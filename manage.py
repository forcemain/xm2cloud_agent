#! -*- coding: utf-8 -*-
import sys
import time
import signal


from agent import settings
from agent.util.logger import Logger
from agent.core.monitor import Monitor
from agent.database import get_agentdir


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, get_agentdir())


logger = Logger.get_logger(__name__)


class Agent(object):
    def __init__(self, channel=None, eventer=None, heatbeat=None, monitor=None):
        self._looping = True
        self._channel = channel
        self._eventer = eventer
        self._heatbeat = heatbeat
        self._monitor = monitor


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
        self._monitor = Monitor()

        return self._monitor

    def start_channel(self):
        self.channel.start()

    def start_eventer(self):
        self.eventer.start()

    def start_heatbeat(self):
        self.heatbeat.start()

    def start_monitor(self):
        self.monitor.start()

    def stop(self, signum, frame):
        logger.warn('got signal {0}, stop'.format(signum))

        self.monitor.stop(force=True)

        self._looping = False

    def run(self):
        self.start_monitor()

    def loop(self):

        self.run()

        for sig in (signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, self.stop)

        while self._looping:
            time.sleep(settings.AGENT_LOOP_INTERVAL)

if __name__ == '__main__':
    Agent().loop()

