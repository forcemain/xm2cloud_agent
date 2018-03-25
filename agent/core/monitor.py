#! -*- coding: utf-8 -*-


import os
import time


from agent import settings
from agent import database
from threadpool import makeRequests
from multiprocessing import Process
from agent.util.logger import Logger
from datetime import datetime, timedelta
from agent.handler.cache import CacheHandler
from agent.handler.monitor import MonitorHandler
from agent.exceptions import GracefulExitException
from agent.metrics.basecollect import BaseCollector


logger = Logger.get_logger(__name__)


class Monitor(Process):
    def __init__(self, gsignal, cache_path=None, monitor_handler=None, eventer_handler=None):
        super(Monitor, self).__init__()

        self._task_map = {}
        self._gsignal = gsignal
        self._wcache_handler = None
        self._cache_path = cache_path
        self._monitor_handler = monitor_handler
        self._eventer_handler = eventer_handler

    @property
    def cache_path(self):
        if self._cache_path is not None and os.path.exists(self._cache_path):
            return self._cache_path
        basedir = database.get_basedir()
        self._cache_path = os.path.join(basedir, 'cache', 'monitor')

        return self._cache_path

    @property
    def wcache_handler(self):
        if isinstance(self._wcache_handler, CacheHandler):
            return self._wcache_handler
        cache_path = self.cache_path
        self._wcache_handler = CacheHandler(cache_path=cache_path)

        return self._wcache_handler

    @property
    def monitor_handler(self):
        if self._monitor_handler:
            return self._monitor_handler
        self._monitor_handler = MonitorHandler()

        return self._monitor_handler

    @property
    def next_scheduled(self):
        next_time = datetime.now() + timedelta(seconds=settings.MONITOR_SCHEDULER_INTERVAL)
        next_time_str = next_time.strftime('%Y-%m-%d %H:%M:%S')

        return next_time_str

    @property
    def eventer_handler(self):
        return self._eventer_handler

    def event_get(self):
        events = []

        for klass in BaseCollector():
            if klass.loader is None:
                args = ()
                kwargs = {}
            else:
                args = klass.loader.init_conf['args'] or ()
                kwargs = klass.loader.init_conf['kwargs'] or {}

            klass_ins = klass(*args, **kwargs)
            events.append(klass_ins)

        return events

    def event_put(self, task, res):
        """
        Todo:
        1. creat event and put it to local cache
        """
        task_data = self._task_map.pop(task.requestID)

        event = task_data.get('event')

        for ins in res:
            print ins

    def run_destructor(self):
        pass

    def event_exp(self, task, err):
        _, exception, _ = err
        task_data = self._task_map.pop(task.requestID)

        event = task_data.get('event')
        logger.error('Call plugin {0} {1}'.format(event.__module__, exception))

    def run(self):
        try:
            while not self._gsignal.is_set():
                events = self.event_get()
                if len(events) == 0:
                    logger.info('No events ready, next scheduled at {0}'.format(self.next_scheduled))
                    time.sleep(settings.MONITOR_SCHEDULER_INTERVAL)
                tasks = makeRequests(self.monitor_handler.run_executer, events, self.event_put, self.event_exp)
                for i, task in enumerate(tasks):
                    self._task_map.update({task.requestID: {
                        'event': events[i]
                    }})
                self.monitor_handler.feed(*tasks)
                time.sleep(settings.MONITOR_SCHEDULER_INTERVAL)
            print 'Monitor process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Monitor process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            import traceback
            print traceback.format_exc()
            print 'Monitor process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()



