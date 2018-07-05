#! -*- coding: utf-8 -*-


import os
import urllib
import shutil


from agent.common.enhance import Pipe
from agent.common.logger import Logger
from agent.common.zipfile import ZipFile
from agent.models.deploy.pub_appspec import PubAppSpec
from agent.handler.deploy.basehandler import BaseDeployHandler


logger = Logger.get_logger(__name__)


class CodeDeployHandler(BaseDeployHandler):
    def deploy(self, event):
        workspace = self.download(event)
        if workspace is None:
            return_code = 1313
            return return_code

        return self.deploy_code(event, workspace)

    def deploy_code(self, event, workspace):
        return_code = 1314 | Pipe(self._application_stop)(event, workspace) |\
                      Pipe(self._download_bundle)(event, workspace) | Pipe(self._before_install)(event, workspace) |\
                      Pipe(self._application_install)(event, workspace) | Pipe(self._after_install)(event, workspace) |\
                      Pipe(self._application_start)(event, workspace) | Pipe(self._validate_service)(event, workspace)

        return return_code
    
    def validate_appspec(self, dpath):
        appspec_path = os.path.join(dpath, 'appspec.json')
        with open(appspec_path, 'r+b') as fd:
            self.appspec = PubAppSpec.from_json(fd.read())

        return self.appspec.is_valid()

    def get_unzip_path(self, event, frelease):
        app_id = event.get_app_id()
        revision_id = event.get_revision_id()
        dpath = os.path.join(self.engine.channel_handler.dcache_path, app_id, revision_id, frelease)

        return dpath

    def force_unzip(self, spath, dpath):
        if not os.path.exists(dpath):
            os.makedirs(dpath)

        z = ZipFile(spath)
        z.extractall(dpath)
        z.close()

    def download_retrieve(self, url, path):
        def _retrieve(blocknum, blocksize, totalsize):
            percent = 100.0 * blocknum * blocksize / totalsize
            percent = 100 if percent > 100 else percent
            _message = 'Download progress: %.2f%%' % (percent,)
            self.engine.info(self.pevent, _message)

        urllib.urlretrieve(url, path, _retrieve)

    def download(self, event):
        workspace = None
        download_url = event.get_download_url()

        self.pevent = event.get_event()
        parent_timestamp = self.pevent.get_event_timestamp()
        frelease = '{0}_release'.format(parent_timestamp)
        filename = '{0}.zip'.format(frelease)
        filepath = os.path.join(self.engine.channel_handler.dcache_path, filename)

        app_name = event.get_app_name()
        app_revision = event.get_app_revision()
        _message = 'Start download application: {0} revision: {1} from {2}'.format(app_name, app_revision, download_url)
        self.engine.info(self.pevent, _message)

        self.download_retrieve(download_url, filepath)

        if os.path.exists(filepath):
            filesize = os.path.getsize(filepath)
            if filesize > 0:
                _message = 'Download to {0} success, filesize: {1}'.format(filepath, filesize)
                self.engine.info(self.pevent, _message)

                spath, dpath = filepath, self.get_unzip_path(event, frelease)
                _message = 'Start unzip {0} to {1}'.format(spath, dpath)
                self.engine.info(self.pevent, _message)
                self.force_unzip(spath, dpath)
                _message = 'Start validate required appspec.json from {0}'.format(dpath)
                self.engine.info(self.pevent, _message)
                is_valid = self.validate_appspec(dpath)
                if is_valid:
                    _message = 'Validate appspec.json from {0} success'.format(dpath)
                    self.engine.info(self.pevent, _message)
                    workspace = dpath
                else:
                    _message = 'Validate appspec.json from {0} failed'.format(dpath)
                    self.engine.error(self.pevent, _message)
                    workspace = workspace

                # reverse 3 backup release
                base_path = os.path.dirname(dpath)
                releases = sorted(os.listdir(base_path), reverse=True)
                for release in releases[3:]:
                    abs_path = os.path.join(base_path, release)
                    shutil.rmtree(abs_path)
                    zip_path = os.path.join(self.engine.channel_handler.dcache_path, '{0}.zip'.format(release))
                    if not os.path.exists(zip_path):
                        continue
                    os.remove(zip_path)
            else:
                _message = 'Download to {0} failed, filesize: {1}'.format(filepath, filesize)
                self.engine.error(self.pevent, _message)
        else:
            _message = 'Download to {0} failed'.format(filepath)
            self.engine.error(self.pevent, _message)

        return workspace

    def _application_stop(self, return_code, event, workspace):
        hook_name = 'application_stop'

        return self._hook_dispatch(hook_name, return_code, event, workspace)

    def _download_bundle(self, return_code, event, workspace):
        hook_name = 'download_bundle'

        return self._hook_dispatch(hook_name, return_code, event, workspace)

    def _before_install(self, return_code, event, workspace):
        hook_name = 'before_install'

        return self._hook_dispatch(hook_name, return_code, event, workspace)

    def _application_install(self, return_code, event, workspace):
        hook_name = 'application_install'

        return self._hook_dispatch(hook_name, return_code, event, workspace)

    def _after_install(self, return_code, event, workspace):
        hook_name = 'after_install'

        return self._hook_dispatch(hook_name, return_code, event, workspace)

    def _application_start(self, return_code, event, workspace):
        hook_name = 'application_start'

        return self._hook_dispatch(hook_name, return_code, event, workspace)

    def _validate_service(self, return_code, event, workspace):
        hook_name = 'validate_service'

        return self._hook_dispatch(hook_name, return_code, event, workspace)
