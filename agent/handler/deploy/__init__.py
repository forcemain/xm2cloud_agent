#! -*- coding: utf-8 -*-


from agent.models.deploy.deploy_type import DeployType
from agent.handler.deploy._code import CodeDeployHandler
from agent.handler.deploy._docker import DockerDeployHandler
from agent.handler.deploy._default import DefaultDeployHandler


class DeployHandlerFactory(object):
    def __init__(self, engine):
        self.engine = engine

    def create_handler(self, name):
        handlers = {
            DeployType.CODE: CodeDeployHandler,
            DeployType.DOCKER: DockerDeployHandler,
        }

        return handlers.get(name, DefaultDeployHandler)(engine=self.engine)
