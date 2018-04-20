#! -*- coding: utf-8 -*-


from agent.util.logger import Logger
from agent.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class DefaultEngineHandler(BaseEngineHandler):
    enable = True
    name = 'default'

    def dispose(self, event):
        self.dispose_notexists(event)
