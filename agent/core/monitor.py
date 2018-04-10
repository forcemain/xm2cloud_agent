#! -*- coding: utf-8 -*-


import os
import time


from agent import settings
from threadpool import makeRequests
from multiprocessing import Process
from agent.util.logger import Logger
from datetime import datetime, timedelta
from agent.metrics.baseloader import BaseLoader
from agent.handler.monitor import MonitorHandler
from agent.exceptions import GracefulExitException
from agent.metrics.basecollect import BaseCollector
from agent.handler.event.monitor import MonitorEventHandler
from agent.handler.channel.rabbitmq import RabbitMQChannelHandler


logger = Logger.get_logger(__name__)


class Monitor(Process):
    def __init__(self, gsignal, monitor_handler=None, event_handler=None, channel_handler=None):
        super(Monitor, self).__init__()

        self._task_map = {}
        self._gsignal = gsignal
        self._event_handler = event_handler
        self._channel_handler = channel_handler
        self._monitor_handler = monitor_handler

    @property
    def monitor_handler(self):
        if isinstance(self._monitor_handler, MonitorHandler):
            return self._monitor_handler
        self._monitor_handler = MonitorHandler()

        return self._monitor_handler

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    @property
    def next_scheduled(self):
        next_time = datetime.now() + timedelta(seconds=settings.MONITOR_SCHEDULER_INTERVAL)
        next_time_str = next_time.strftime('%Y-%m-%d %H:%M:%S')

        return next_time_str

    @property
    def event_handler(self):
        if isinstance(self._event_handler, MonitorEventHandler):
            return self._event_handler
        self._event_handler = MonitorEventHandler()

        return self._event_handler

    def event_get(self):
        events = []

        for klass in BaseCollector():
            if not isinstance(klass.loader, BaseLoader):
                args = ()
                kwargs = {}
            else:
                args = klass.loader.init_conf['args'] or ()
                kwargs = klass.loader.init_conf['kwargs'] or {}

            klass_ins = klass(*args, **kwargs)
            events.append(klass_ins)

        return events

    def event_put(self, task, res):
        self._task_map.pop(task.requestID)

        for ins in res:
            if not ins.is_valid():
                logger.warning('Invalid monitor event data: {0}'.format(ins))
                continue
            logger.debug('Verified monitor event data: {0}'.format(ins))
            event = self.event_handler.create_event(ins.to_json())

            self.channel_handler.wcache_handler.write(event.to_json())

    def run_destructor(self):
        pass

    def event_exp(self, task, err):
        _, exception, _ = err
        task_data = self._task_map.pop(task.requestID)

        event = task_data.get('event')
        logger.error('Call plugin {0} {1}'.format(event.real_name, exception))

    def run(self):
        try:
            while not self._gsignal.is_set():
                events = self.event_get()
                if len(events) == 0:
                    logger.info('No events ready, next scheduled at {0}'.format(self.next_scheduled))
                    time.sleep(settings.MONITOR_SCHEDULER_INTERVAL)
                    continue
                tasks = makeRequests(self.monitor_handler.run_executer, events, self.event_put, self.event_exp)
                for i, task in enumerate(tasks):
                    self._task_map.update({task.requestID: {'event': events[i]}})
                self.monitor_handler.feed(*tasks)
                time.sleep(settings.MONITOR_SCHEDULER_INTERVAL)
            print 'Monitor process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Monitor process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Monitor process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()
