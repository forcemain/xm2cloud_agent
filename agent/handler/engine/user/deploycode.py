#! -*- coding: utf-8 -*-


from agent.common.logger import Logger
from agent.models.event.event_type import EventType
from agent.handler.engine.baseengine import BaseEngineHandler

logger = Logger.get_logger(__name__)


class DeployCodeEngineHandler(BaseEngineHandler):
    enable = False
    name = EventType.DEPLOYCODE

    def handle(self, event):
        pass
