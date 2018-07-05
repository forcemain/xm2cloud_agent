#! -*- coding: utf-8 -*-


from agent.common.logger import Logger
from agent.models.event.event_type import EventType
from agent.models.deploy.pub_deploy import PubDeploy
from agent.handler.deploy import DeployHandlerFactory
from agent.handler.engine.baseengine import BaseEngineHandler

logger = Logger.get_logger(__name__)


class DeployCodeEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.DEPLOYCODE

    def __init__(self, *args, **kwargs):
        event_handler = kwargs.get('event_handler', None)
        channel_handler = kwargs.get('channel_handler', None)
        super(DeployCodeEngineHandler, self).__init__(event_handler=event_handler,
                                                      channel_handler=channel_handler)

        self._deploy_factory = kwargs.get('deploy_factory', None)

    @property
    def deploy_factory(self):
        if isinstance(self._deploy_factory, DeployHandlerFactory):
            return self._deploy_factory
        self._deploy_factory = DeployHandlerFactory(engine=self)

        return self._deploy_factory

    def handle(self, event):
        logger.info('{0} handle event: {1}'.format(self.real_name, event))
        event_data = event.get_event_data()
        deploy_event = PubDeploy.from_json(event_data)

        if not deploy_event.is_valid():
            logger.warning('{0} got invalid deploy event: {1}'.format(self.real_name, event_data))
            return_code = 1313

            return return_code

        deploy_type = deploy_event.get_app_type()
        deploy_handler = self.deploy_factory.create_handler(deploy_type)
        logger.debug('{0}  deploy {1}: {2}'.format(self.real_name, deploy_type, event_data))
        deploy_event.set_event(event)
        return_code = deploy_handler.deploy(deploy_event)

        return return_code
