#! -*- coding: utf-8 -*-


import os
import time
import tempfile
import subprocess


from agent.util.logger import Logger
from agent.models.event.user_script import UserScript
from agent.handler.engine.baseengine import BaseEngineHandler

logger = Logger.get_logger(__name__)


class ExecuteScriptEngineHandler(BaseEngineHandler):
    enable = True
    name = 'execute_script'

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

        script_file, script_obj = self.get_uscript(event)
        command = '{0} {1}'.format(script_obj.get_interpreter(), script_file.name)
        os.environ.update({'PYTHONIOENCODING': 'utf-8'})
        p = subprocess.Popen(command, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             env=os.environ)
        p_timeout = script_obj.get_timeout()
        p_running = time.time()
        interrupt = False
        while p.poll() is None:
            p_during = time.time() - p_running
            if p_during > p_timeout:
                p.terminate()
                interrupt = True
            logger.debug('Event: {0}(timeout: {1}s) left {2} secomnds force exit'.format(
                event_id, p_timeout, p_timeout - p_during
            ))
            self.info(event, p.stdout.readline())
        if interrupt is False and p.returncode != 0:
            map(lambda err: self.error(event, err), p.stderr)
        try:
            script_file.close()
        finally:
            pass

        return p.returncode






