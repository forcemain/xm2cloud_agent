#! -*- coding: utf-8 -*-


import os
import sys
import signal


from multiprocessing import Event
from agent.exceptions import GracefulExitException


class GracefulExitSignal(object):
    def __init__(self, event=None):
        self.workers = []
        self.event = event or Event()

        for sig in (signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, GracefulExitException.exitsig_handler)

    def set(self):
        self.event.set()

    def is_set(self):
        return self.event.is_set()

    def register_workers(self, *workers):
        if len(workers) == 0:
            return

        for worker in workers:
            if worker in self.workers:
                continue
            self.workers.append(worker)

    def listening(self):
        try:
            for worker in self.workers:
                worker.join()
            print 'Main process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Main process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Main process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            sys.exit(0)
