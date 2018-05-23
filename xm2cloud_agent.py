#! -*- coding: utf-8 -*-


import sys


from agent.core.engine import Engine
from agent.common.logger import Logger
from agent.core.monitor import Monitor
from agent.core.channel import Channel
from agent.database import get_agentdir
from agent.core.heatbeat import Heartbeat
from agent.signals.exit import GracefulExitSignal


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, get_agentdir())


logger = Logger.get_logger(__name__)


class Agent(object):
    def __init__(self, channel=None, engine=None, heatbeat=None, monitor=None):
        self._engine = engine
        self._monitor = monitor
        self._channel = channel
        self._heatbeat = heatbeat

        self._gsignal = GracefulExitSignal()

    @property
    def engine(self):
        if isinstance(self._engine, Engine):
            return self._engine
        self._engine = Engine(self._gsignal)

        return self.engine

    @property
    def channel(self):
        if isinstance(self._channel, Channel):
            return self._channel
        self._channel = Channel(self._gsignal)

        return self._channel

    @property
    def heatbeat(self):
        if isinstance(self._heatbeat, Heartbeat):
            return self._heatbeat
        self._heatbeat = Heartbeat(self._gsignal)

        return self._heatbeat

    @property
    def monitor(self):
        if self._monitor:
            return self._monitor
        self._monitor = Monitor(self._gsignal)

        return self._monitor

    def run(self):
        self.engine.start()
        self.monitor.start()
        self.channel.start()
        self.heatbeat.start()

    def start(self):
        self.run()
        self._gsignal.register_workers(*[
            self.engine,
            self.monitor,
            self.channel,
            self.heatbeat,
        ])

    def listening(self):
        self.start()
        self._gsignal.listening()

if __name__ == '__main__':
    Agent().listening()
