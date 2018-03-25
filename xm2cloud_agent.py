#! -*- coding: utf-8 -*-


import sys


from agent.util.logger import Logger
from agent.core.monitor import Monitor
from agent.database import get_agentdir
from agent.signals.exit import GracefulExitSignal


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, get_agentdir())


logger = Logger.get_logger(__name__)


class Agent(object):
    def __init__(self, channel=None, eventer=None, heatbeat=None, monitor=None):
        self._channel = channel
        self._eventer = eventer
        self._heatbeat = heatbeat
        self._monitor = monitor

        self._gsignal = GracefulExitSignal()

    @property
    def channel(self):
        return self._channel

    @property
    def eventer(self):
        return self._eventer

    @property
    def heatbeat(self):
        return self._eventer

    @property
    def monitor(self):
        if self._monitor:
            return self._monitor
        self._monitor = Monitor(self._gsignal)

        return self._monitor

    def run(self):
        self.monitor.start()

    def start(self):
        self.run()
        self._gsignal.register_workers(*[
            self.monitor
        ])

    def listening(self):
        self.start()
        self._gsignal.listening()

if __name__ == '__main__':
    Agent().listening()
