#! -*- coding: utf-8 -*-


import os
import time


from agent import settings
from threading import Thread
from multiprocessing import Process
from agent.util.logger import Logger
from datetime import datetime, timedelta
from agent.models.event.pub_event import PubEvent
from agent.exceptions import GracefulExitException
from agent.handler.event.engine import EngineEventHandler
from agent.handler.channel.rabbitmq import RabbitMQChannelHandler


logger = Logger.get_logger(__name__)


class EventThread(Thread):
    def __init__(self, event_data, obj):
        super(EventThread, self).__init__()

        self._obj = obj
        self._fname, self._fcontent = event_data

    def run(self):
        try:
            event = PubEvent.from_json(self._fcontent)
            self._obj.event_dispatch(event)
        except Exception as e:
            logger.error('Handler %s got unexpected Exception %s', self._fname, e)
        finally:
            self._obj.channel_handler.rcache_handler.remove(self._fname)


class Engine(Process):
    def __init__(self, gsignal, engine_handler=None, channel_handler=None, event_handler=None):
        super(Engine, self).__init__()

        self._gsignal = gsignal
        self._event_handler = event_handler
        self._engine_handler = engine_handler
        self._channel_handler = channel_handler

    @property
    def engine_handler(self):
        return self._engine_handler

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    @property
    def event_handler(self):
        if isinstance(self._event_handler, EngineEventHandler):
            return self._event_handler
        self._event_handler = EngineEventHandler()

        return self._event_handler

    @property
    def next_scheduled(self):
        next_time = datetime.now() + timedelta(seconds=settings.ENGINE_SCHEDULER_INTERVAL)
        next_time_str = next_time.strftime('%Y-%m-%d %H:%M:%S')

        return next_time_str

    def run_destructor(self):
        pass

    def event_get(self):
        # default batch is 50, can be set larger
        events_data = self.channel_handler.rcache_handler.read()

        return events_data

    def event_dispatch(self, event):
        # Todo:
        #   1. dispatch event with eventfactory
        #   2. logging event lifecycle log and asynchronous send
        #   3. event test
        #       3.1. is valid ?
        #       3.2. is expired ? ( half hour ago. )
        #       3.3. is choreography ? ( handler later. )
        #
        pass

    def run(self):
        try:
            while not self._gsignal.is_set():
                events_data = self.event_get()
                if len(events_data) == 0:
                    logger.info('No events ready, next scheduled at {0}'.format(self.next_scheduled))
                    time.sleep(settings.ENGINE_SCHEDULER_INTERVAL)
                    continue
                events_task = []
                for event_data in events_data:
                    t = EventThread(event_data, self)
                    t.setDaemon(True)
                    t.start()
                    events_task.append(t)
                for event_task in events_task:
                    event_task.join()
                time.sleep(settings.ENGINE_SCHEDULER_INTERVAL)
            print 'Engine process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Engine process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Engine process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()

