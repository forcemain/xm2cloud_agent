#! -*- coding: utf-8 -*-


import os
import time


from traceback import format_exc


from agent import settings
from threading import Thread
from functools import partial
from multiprocessing import Process
from agent.util.logger import Logger
from agent.util.amqp.status import AMQPStatus
from agent.exceptions import GracefulExitException
from agent.handler.channel.rabbitmq import RabbitMQChannelHandler


logger = Logger.get_logger(__name__)


class Channel(Process):
    def __init__(self, gsignal, channel_handler=None):
        super(Channel, self).__init__()

        self._gsignal = gsignal
        self._channel_handler = channel_handler

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    def run_destructor(self):
        try:
            self.channel_handler.msg_sender.stop()
            self.channel_handler.msg_receiver.stop()
        finally:
            pass

    def thread_exp(self, name, func):
        try:
            func()
        except Exception as e:
            print '=' * 100
            print format_exc()
            print '=' * 100
            logger.error('%s got unexpected Exception %s', name, e)

    def sender_thread(self):
        target = partial(self.thread_exp, 'Channel sender', self.channel_handler.msg_sender.run)
        t = Thread(target=target)
        t.setDaemon(True)
        
        return t

    def receiver_thread(self):
        target = partial(self.thread_exp, 'Channel receiver', self.channel_handler.msg_receiver.run)
        t = Thread(target=target)
        t.setDaemon(True)

        return t

    def channel_checking(self):
        if self.channel_handler.msg_sender.connection_status == AMQPStatus.DISCONNECTED:
            logger.warning('Channel sender status, %s', AMQPStatus.DISCONNECTED)
        if self.channel_handler.msg_receiver.connection_status == AMQPStatus.DISCONNECTED:
            logger.warning('Channel receiver status, %s', AMQPStatus.DISCONNECTED)

        logger.debug('Go check channel sender disconnected')
        sender_disconnect_time = self.channel_handler.msg_sender.disconnect_time
        if sender_disconnect_time is not None:
            logger.debug('Channel sender disconnect time, %f', sender_disconnect_time)
            if time.time() - sender_disconnect_time > 60:
                try:
                    self.channel_handler.msg_sender.stop()
                except Exception as e:
                    logger.error('Channel sender stop with unexpected error, %s', e)
                finally:
                    self.sender_thread().start()
        logger.debug('Go check channel receiver disconnected')
        receiver_disconnect_time = self.channel_handler.msg_receiver.disconnect_time
        if receiver_disconnect_time is not None:
            logger.debug('Channel sender disconnect time, %f', sender_disconnect_time)
            if time.time() - receiver_disconnect_time > 60:
                try:
                    self.channel_handler.msg_receiver.stop()
                except Exception as e:
                    logger.error('Channel receiver stop with unexpected error, %s', e)
                finally:
                    self.receiver_thread().start()

    def run(self):
        # start sender and receiver thread
        self.sender_thread().start()
        self.receiver_thread().start()
        try:
            while not self._gsignal.is_set():
                self.channel_checking()
                time.sleep(settings.CHANNEL_SCHEDULER_INTERVAL)
            print 'Channel process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Channel process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Channel process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()
