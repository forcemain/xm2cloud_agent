#! -*- coding: utf-8 -*-


import os
import time
import fcntl
import signal
import tempfile
import subprocess


from agent.common.logger import Logger
from agent.models.event.event_type import EventType
from agent.models.event.user_script import UserScript
from agent.handler.engine.baseengine import BaseEngineHandler

logger = Logger.get_logger(__name__)


class ExecuteScriptEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.EXECUTESCRIPT

    def get_uscript(self, event):
        script_file, script_obj = None, None
        event_data = event.get_event_data()
        userscript = UserScript.from_json(event_data)

        if not userscript.is_valid():
            logger.warning('{0} got invalid user script: {1}'.format(self.real_name, event_data))
            return script_file, script_obj

        script_file = tempfile.NamedTemporaryFile(delete=True)
        script_file.write(userscript.get_scripttext())
        script_file.flush()
        script_file.seek(0)
        script_obj = userscript

        return script_file, script_obj

    def handle(self, event):
        logger.info('{0} handle event: {1}'.format(self.real_name, event))

        event_id = event.get_event_id()
        event_data = event.get_event_data()
        logger.debug('{0} execute script: {1}'.format(self.real_name, event_data))

        return_code = 1314
        script_file, script_obj = self.get_uscript(event)
        command = '{0} {1}'.format(script_obj.get_interpreter(), script_file.name)
        os.environ.update({'PYTHONIOENCODING': 'utf-8'})
        p = subprocess.Popen(command, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             preexec_fn=os.setsid, env=os.environ)
        fd = p.stdout.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

        interrupt = False
        p_running = time.time()
        p_timeout = int(script_obj.get_timeout())
        while True:
            p_during = time.time() - p_running
            if p_during > p_timeout:
                p.terminate()
                p.wait()
                try:
                    os.killpg(p.pid, signal.SIGTERM)
                except OSError:
                    pass
                interrupt = True
                return_code = 1312
                break
            logger.debug('Event: {0}(timeout: {1}s) left {2} secomnds force exit'.format(
                event_id, p_timeout, p_timeout - p_during
            ))
            try:
                line = p.stdout.readline()
            except IOError:
                time.sleep(0.1)
                continue
            if line == b'' and p.poll() is not None:
                break
            self.info(event, line)
        if interrupt is False and p.returncode != 0:
            return_code = 1313
            while True:
                line = p.stderr.readline()
                if line == b'':
                    break
                self.error(event, line)
        try:
            script_file.close()
        except (IOError, OSError):
            pass

        return return_code






