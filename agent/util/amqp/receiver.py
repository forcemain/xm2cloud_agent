# -*- coding: utf-8 -*-


import time


from agent.util.logger import Logger
from agent.util.amqp.status import AMQPStatus


logger = Logger.get_logger(__name__)


class AMQPReceiver(object):
    def __init__(self, **kwargs):
        self._channel = None
        self._closing = False
        self._connection = None
        self._consumer_tag = None
        self._queue = kwargs.get('queue', None)
        self._exchange = kwargs.get('exchange', None)
        self._count_down = kwargs.get('count_down', 5)
        self._routing_key = kwargs.get('routing_key', None)
        self._exchange_type = kwargs.get('exchange_type', None)

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
        if not self._closing:
            self._connection = self.connect()
            self._connection.ioloop.start()

    def open_channel(self):
        logger.info('Creating a new channel')
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        logger.info('Channel opened')
        self._channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange(self._exchange)

        # start consuming when channel open
        self.start_consuming()

    def add_on_channel_close_callback(self):
        logger.info('Adding channel close callback')
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reply_code, reply_text):
        logger.warning('Channel %i was closed: (%s) %s',
                       channel, reply_code, reply_text)
        self._connection.close()

    def setup_exchange(self, exchange_name):
        logger.info('Declaring exchange %s', exchange_name)
        self._channel.exchange_declare(self.on_exchange_declareok,
                                       exchange_name,
                                       self._exchange_type)

    def on_exchange_declareok(self, unused_frame):
        logger.info('Exchange declared')
        self.setup_queue(self._queue)

    def setup_queue(self, queue_name):
        logger.info('Declaring queue %s', queue_name)
        self._channel.queue_declare(self.on_queue_declareok, queue_name)

    def on_queue_declareok(self, method_frame):
        logger.info('Binding %s to %s with %s',
                    self._exchange, self._queue, self._routing_key)
        self._channel.queue_bind(self.on_bindok, self._queue,
                                 self._exchange, self._routing_key)

    def on_bindok(self, unused_frame):
        logger.info('Queue bound')
        self.start_consuming()

    def start_consuming(self):
        logger.info('Issuing consumer related RPC commands')
        self.add_on_cancel_callback()
        self._consumer_tag = self._channel.basic_consume(self.on_message,
                                                         self._queue)

    def add_on_cancel_callback(self):
        logger.info('Adding consumer cancellation callback')
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame):
        logger.info('Consumer was cancelled remotely, shutting down: %r',
                    method_frame)
        if self._channel:
            self._channel.close()

    def on_message(self, unused_channel, basic_deliver, properties, body):
        raise NotImplementedError

    def acknowledge_message(self, delivery_tag):
        logger.info('Acknowledging message %s', delivery_tag)
        self._channel.basic_ack(delivery_tag)

    def stop_consuming(self):
        if self._channel:
            logger.info('Sending a Basic.Cancel RPC command to RabbitMQ')
            self._channel.basic_cancel(self.on_cancelok, self._consumer_tag)

    def on_cancelok(self, unused_frame):
        logger.info('RabbitMQ acknowledged the cancellation of the consumer')
        self.close_channel()

    def close_channel(self):
        logger.info('Closing the channel')
        self._channel.close()

    def run(self):
        self._connection = self.connect()
        self._connection.ioloop.start()

    def stop(self):
        logger.info('Stopping')
        self._closing = True
        self.stop_consuming()
        self._connection.ioloop.stop()
        logger.info('Stopped')

    def close_connection(self):
        logger.info('Closing connection')
        self._connection.close()
