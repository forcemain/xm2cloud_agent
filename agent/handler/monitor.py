#! -*- coding: utf-8 -*-


import multiprocessing


from concurrent import futures
from agent.metrics import host
from agent.metrics import user
from threadpool import ThreadPool
from agent.util.logger import Logger


logger = Logger.get_logger(__name__)


class MonitorHandler(object):
    def __init__(self):
        self._pool = None

    @property
    def pool(self):
        if isinstance(self._pool, ThreadPool):
            return self._pool
        self._pool = ThreadPool(self.get_maxworks())

        return self._pool

    def get_maxworks(self):
        return multiprocessing.cpu_count()*4

    def run_executer(self, event):
        results = event.start_collects()

        return results

    def feed(self, *tasks):
        map(lambda t: self.pool.putRequest(t), tasks)

        self.pool.wait()



