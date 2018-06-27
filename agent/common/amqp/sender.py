# -*- coding: utf-8 -*-


import time


from agent.common.logger import Logger
from agent.common.amqp.status import AMQPStatus


logger = Logger.get_logger(__name__)


class AMQPSender(object):
    def __init__(self, **kwargs):
        self._channel = None
        self._closing = False
        self._stopping = False
        self._connection = None
        self._queue = kwargs.get('queue', None)
        self._exchange = kwargs.get('exchange', None)
        self._routing_key = kwargs.get('routing_key')
        self._count_down = kwargs.get('count_down', 5)
        self._exchange_type = kwargs.get('exchange_type')
        self._publish_interval = kwargs.get('publish_interval', 1)

        # get a millisecond timestamp
        self._disconnect_time = int(time.time())
        self._connection_status = AMQPStatus.DISCONNECTED

    @property
    def disconnect_time(self):
        return self._disconnect_time

    @property
    def connection_status(self):
        return self._connection_status

    def connect(self):
        raise NotImplementedError

    def on_connection_open(self, unused_connection):
        logger.info('Connection opened')

        # update disconnect time and current connect status
        self._disconnect_time = None
        self._connection_status = AMQPStatus.CONNECTED

        self.add_on_connection_close_callback()
        self.open_channel()

    def add_on_connection_close_callback(self):
        logger.info('Adding connection close callback')
        self._connection.add_on_close_callback(self.on_connection_closed)

    def on_connection_closed(self, connection, reply_code, reply_text):
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
        else:
            logger.warning('Connection closed, reopening in 5 seconds: (%s) %s',
                           reply_code, reply_text)

            # update disconnect time and current connect status
            self._disconnect_time = None
            self._connection_status = AMQPStatus.CONNECTED

            self._connection.add_timeout(self._count_down, self.reconnect)

    def reconnect(self):
        self._connection.ioloop.stop()

        self._connection = self.connect()
        self._connection.ioloop.start()

    def open_channel(self):
        logger.info('Creating a new channel')
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        logger.info('Channel opened')
        self._channel = channel
        self.add_on_channel_close_callback()
        # enable delivery ack and start publish
        self.start_publishing()

    def add_on_channel_close_callback(self):
        logger.info('Adding channel close callback')
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        logger.warning('Channel was closed: (%s) %s', reply_code, reply_text)
        if not self._closing:
            self._connection.close()

    def start_publishing(self):
        logger.info('Issuing consumer related RPC commands')
        self.schedule_next_message()

    def schedule_next_message(self):
        if self._stopping:
            return
        logger.info('Scheduling next message for %0.1f seconds',
                    self._publish_interval)
        self._connection.add_timeout(self._publish_interval,
                                     self.publish_message)

    def publish_message(self):
        raise NotImplementedError

    def close_channel(self):
        logger.info('Closing the channel')
        if self._channel:
            self._channel.close()

    def run(self):
        self._connection = self.connect()
        self._connection.ioloop.start()

    def stop(self):
        logger.info('Stopping')
        self._stopping = True
        self.close_channel()
        self.close_connection()
        self._connection.ioloop.stop()
        logger.info('Stopped')

    def close_connection(self):
        logger.info('Closing connection')
        self._closing = True
        self._connection.close()
