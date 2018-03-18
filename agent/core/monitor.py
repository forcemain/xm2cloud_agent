#! -*- coding: utf-8 -*-


from agent import settings
from agent.util.logger import Logger
from apscheduler.scheduler import Scheduler
from agent.handler.monitor import MonitorHandler


logger = Logger.get_logger(__name__)


class Monitor(object):
    def __init__(self, cache_path=None, monitor_handler=None, eventer_handler=None):
        self._cache_path = cache_path
        self._monitor_handler = monitor_handler
        self._eventer_handler = eventer_handler

        self.scheduler = Scheduler()
        self.scheduler.daemonic = False

    @property
    def cache_path(self):
        return self._cache_path

    @property
    def monitor_handler(self):
        if self._monitor_handler:
            return self._monitor_handler
        self._monitor_handler = MonitorHandler()

        return self._monitor_handler

    @property
    def eventer_handler(self):
        return self._eventer_handler

    def put_res_tocache(self, future):
        """
        Todo: put callback result to local cache
        1. create event obj
        2. write event obj enc json data to local cache
        """
        for metric in future.result():
            print metric

    def stop(self, force=False):
        self.scheduler.shutdown(wait=force)

    def start(self):
        self.run()

    def run(self):
        interval = settings.MONITOR_SCHEDULER_INTERVAL

        self.monitor_handler.add_callback(self.put_res_tocache)
        self.scheduler.add_interval_job(self.monitor_handler.to_summarise, seconds=interval)

        self.scheduler.start()


