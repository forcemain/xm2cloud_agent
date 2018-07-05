#! -*- coding: utf-8 -*-


import os
import time
import fcntl
import signal
import subprocess


from agent.common.logger import Logger


logger = Logger.get_logger(__name__)


class BaseDeployHandler(object):
    def __init__(self, engine=None):
        self._specs = None
        self.pevent = None
        self.engine = engine

    @property
    def appspec(self):
        return self._specs

    @appspec.setter
    def appspec(self, appspec):
        self._specs = appspec

    def deploy(self, event):
        raise NotImplementedError

    def download(self, event):
        raise NotImplementedError

    def _hook_dispatch(self, hook_name, return_code, event, workspace):
        return_code = return_code
        if return_code != 1314:
            return return_code

        hooks = event.get_hooks()
        if hook_name not in hooks or len(hooks[hook_name]) == 0:
            return_code = 1314
            _message = 'Not found {0} hook scripts, skipped'.format(hook_name)
            self.engine.error(self.pevent, _message)
            return return_code

        _scripts = hooks[hook_name]
        _message = 'Load {0} hook scripts ... '.format(hook_name)
        self.engine.info(self.pevent, _message)
        for script in _scripts:
            if 'timeout' not in script or 'location' not in script:
                _message = 'Invalid {0} hook script, (timeout, location) required'.format(hook_name)
                self.engine.error(self.pevent, _message)
                return_code = 1313
                break
            script_timeout, script_location = script['timeout'], script['location']
            script_file = os.path.join(workspace, script_location)
            command = 'sh {0} 2>&1'.format(script_file)
            os.environ.update({'PYTHONIOENCODING': 'utf-8'})
            p = subprocess.Popen(command, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 preexec_fn=os.setsid, env=os.environ, cwd=workspace)
            fd = p.stdout.fileno()
            fl = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

            interrupt = False
            p_running = time.time()
            p_timeout = int(script_timeout)
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
                logger.debug('Script: {0}(timeout: {1}s) left {2} secomnds force exit'.format(
                    script_file, p_timeout, p_timeout - p_during
                ))
                try:
                    line = p.stdout.readline()
                except IOError:
                    time.sleep(0.1)
                    continue
                if line == b'' and p.poll() is not None:
                    break
                self.engine.info(self.pevent, line)
            if interrupt is False and p.returncode != 0:
                return_code = 1313
                while True:
                    line = p.stderr.readline()
                    if line == b'':
                        break
                    self.engine.error(self.pevent, line)

            if return_code != 1314:
                break

        return return_code

    def _application_stop(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def _download_bundle(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def _before_install(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def _application_install(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def _after_install(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def _application_start(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def _validate_service(self, return_code, event, workspace):
        return_code = 1313

        return return_code

    def deployer_notexists(self, event):
        parent_event = event.get_event()
        event_name = event.get_app_name()
        message = 'No deploy handler handle event: {0}'.format(event_name)

        logger.warning(message)
        self.engine.async_logging('WARN', parent_event, message)
