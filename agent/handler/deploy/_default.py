#! -*- coding: utf-8 -*-


from agent.common.logger import Logger
from agent.handler.deploy.basehandler import BaseDeployHandler


logger = Logger.get_logger(__name__)


class DefaultDeployHandler(BaseDeployHandler):
    def deploy(self, event):
        return_code = 1314

        self.deployer_notexists(event)

        return return_code

    def download(self, event):
        pass
