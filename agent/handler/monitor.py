#! -*- coding: utf-8 -*-


import multiprocessing


from concurrent import futures
from agent.metrics import host
from agent.metrics import user
# automatic reload metric class
"""
example:
    host.autodiscover()
    user.autodiscover()
"""
from agent.util.logger import Logger
from agent.metrics.basecollect import BaseCollector


logger = Logger.get_logger(__name__)


class MonitorHandler(object):
    def __init__(self):
        self.callbacks = []

    def get_maxworks(self):
        collects = self.get_collects()

        return min(multiprocessing.cpu_count()*4, len(collects))

    def get_collects(self):
        collects = []

        for klass in BaseCollector():
            if klass.loader is None:
                args = ()
                kwargs = {}
            else:
                args = klass.loader.init_conf['args'] or ()
                kwargs = klass.loader.init_conf['kwargs'] or {}

            klass_ins = klass(*args, **kwargs)
            collects.append(klass_ins)

        return collects

    def add_callback(self, callback):
        if callback in self.callbacks:
            return
        self.callbacks.append(callback)

    def to_summarise(self):
        metrics = []

        collects = self.get_collects()
        maxworks = self.get_maxworks()
        if not collects:
            return

        with futures.ThreadPoolExecutor(max_workers=maxworks) as executer:
            future_map = {}
            for collect in collects:
                cfuture = executer.submit(collect.start_collects)
                map(cfuture.add_done_callback, self.callbacks)
                future_map[cfuture] = collect
            for future in futures.as_completed(future_map):
                collect = future_map[future]
                try:
                    metrics.extend(future.result())
                except Exception as e:
                    print 'future {0} {1}'.format(collect, e)
                    logger.error('future {0} {1}'.format(collect, e))
        return metrics


