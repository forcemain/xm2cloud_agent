#! -*- coding: utf-8 -*-


from agent.common.logger import Logger
from agent.handler.deploy.basehandler import BaseDeployHandler

logger = Logger.get_logger(__name__)


class DockerDeployHandler(BaseDeployHandler):
    def deploy(self, event):
        pass

    def download(self, event):
        pass
