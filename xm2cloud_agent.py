#! -*- coding: utf-8 -*-


import sys


from agent.util.logger import Logger
from agent.core.monitor import Monitor
from agent.core.channel import Channel
from agent.database import get_agentdir
from agent.signals.exit import GracefulExitSignal


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, get_agentdir())


logger = Logger.get_logger(__name__)


class Agent(object):
    def __init__(self, channel=None, event=None, heatbeat=None, monitor=None):
        self._event = event
        self._channel = channel
        self._heatbeat = heatbeat
        self._monitor = monitor

        self._gsignal = GracefulExitSignal()

    @property
    def event(self):
        return self._event

    @property
    def channel(self):
        if isinstance(self._channel, Channel):
            return self._channel
        self._channel = Channel(self._gsignal)

        return self._channel

    @property
    def heatbeat(self):
        return self._event

    @property
    def monitor(self):
        if self._monitor:
            return self._monitor
        self._monitor = Monitor(self._gsignal)

        return self._monitor

    def run(self):
        self.monitor.start()
        self.channel.start()

    def start(self):
        self.run()
        self._gsignal.register_workers(*[
            self.monitor,
            self.channel
        ])

    def listening(self):
        self.start()
        self._gsignal.listening()

if __name__ == '__main__':
    Agent().listening()
