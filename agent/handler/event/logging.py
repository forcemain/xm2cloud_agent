#! -*- coding: utf-8 -*-

import time
import threading
import multiprocessing


from agent.handler.event import BaseEventHandler
from agent.models.event.event_type import EventType
from agent.models.event.handle_log import HandleLog
from agent.handler.event.engine import EngineEventHandler


class LoggingEventHandler(BaseEventHandler):
    def create_event(self, levelname, message):
        logger_event = HandleLog()
        event_engine = EngineEventHandler()
        engine_event = event_engine.create_event(EventType.LOGGING)

        logger_event.set_created(int(time.time()))
        logger_event.set_asctime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        logger_event.set_threadname(threading.current_thread().name)
        logger_event.set_thread(threading.currentThread().ident)
        logger_event.set_process(multiprocessing.current_process().ident)
        logger_event.set_message(message)

        # may be you want encrypt the data
        enc_method, event_data = self.encrypt_data(logger_event.to_json())
        engine_event.set_enc_method(enc_method)
        engine_event.set_event_data(event_data)

        return engine_event

