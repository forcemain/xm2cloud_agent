#! -*- coding: utf-8 -*-


import os
import time


from agent import settings
from threading import Thread
from multiprocessing import Process
from agent.common.enhance import File
from agent.common.logger import Logger
# autodiscovery engine handler
from agent.handler.engine import host
from agent.handler.engine import user
from datetime import datetime, timedelta
from agent.models.event.pub_event import PubEvent
from agent.exceptions import GracefulExitException
from agent.handler.event.engine import EngineEventHandler
from agent.handler.engine.baseengine import EngineHandlerFactory
from agent.handler.channel.rabbitmq import RabbitMQChannelHandler


_evnet_threads = []


logger = Logger.get_logger(__name__)


class EventThread(Thread):
    def __init__(self, event_data, obj):
        super(EventThread, self).__init__()

        self._obj = obj
        self._fname, self._fcontent = event_data

    def after_run(self):
        if self in _evnet_threads:
            _evnet_threads.remove(self)
        self._obj.channel_handler.ccache_handler.remove(self._fname)

    def before_run(self):
        source_file = self._obj.channel_handler.rcache_handler.abspath(self._fname)
        target_file = self._obj.channel_handler.ccache_handler.abspath(self._fname)

        File.force_move(source_file, target_file)

    def run(self):
        self.before_run()
        try:
            event = PubEvent.from_json(self._fcontent)
            self._obj.event_dispatch(event)
        except Exception as e:
            logger.error('Handler %s got unexpected Exception %s', self._fname, e)
        finally:
            self.after_run()


class Engine(Process):
    def __init__(self, gsignal, engine_factory=None, channel_handler=None, event_handler=None):
        super(Engine, self).__init__()

        self._gsignal = gsignal
        self._event_handler = event_handler
        self._engine_factory = engine_factory
        self._channel_handler = channel_handler
        self._userdata = self.channel_handler.userdata_dao.get_user_data()

    @property
    def engine_factory(self):
        if isinstance(self._engine_factory, EngineHandlerFactory):
            return self._engine_factory
        self._engine_factory = EngineHandlerFactory()

        return self._engine_factory

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    @property
    def event_handler(self):
        if isinstance(self._event_handler, EngineEventHandler):
            return self._event_handler
        self._event_handler = EngineEventHandler()

        return self._event_handler

    @property
    def next_scheduled(self):
        next_time = datetime.now() + timedelta(seconds=settings.ENGINE_SCHEDULER_INTERVAL)
        next_time_str = next_time.strftime('%Y-%m-%d %H:%M:%S')

        return next_time_str

    def run_destructor(self):
        self.channel_handler.ccache_handler.clear()

    def event_get(self):
        # default batch is 50, can be set larger
        events_data = self.channel_handler.rcache_handler.read()

        return events_data

    def require_handle(self, event):
        # get source from userdata event
        host_id = self._userdata.get_host_id()
        cluster_id = self._userdata.get_cluster_id()
        hostgroup_id = self._userdata.get_hostgroup_id()

        # get target_... from server event
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        # is it my task ?
        if isinstance(target_host_id, list) and host_id in target_host_id:
            return True
        if isinstance(target_hostgroup_id, list) and isinstance(hostgroup_id, list) and (
            set(target_hostgroup_id) & set(hostgroup_id)
        ):
            return True
        if isinstance(target_cluster_id, list) and isinstance(cluster_id, list) and (
            set(target_cluster_id) & set(cluster_id)
        ):
            return True

        return False

    def allow_dispatch(self, event):
        is_allow = True

        if not self.require_handle(event):
            is_allow = False
            logger.warning('Not own engien event data: {0}'.format(event))
        if event.is_adjunct():
            is_allow = False
            # self.event_response(event, retcode=0)
            logger.warning('Adjunct engine event data: {0}'.format(event))
        if not event.is_valid():
            is_allow = False
            logger.warning('Invalid engine event data: {0}'.format(event))
        # default expired 180s
        if event.is_expired():
            is_allow = False
            logger.warning('Expired engine event data: {0}'.format(event))

        return is_allow

    def event_history(self):
        """May be you want local history
        """
        pass

    def event_response(self, event, retcode=0):
        handled_event_id = event_id = event.get_event_id()
        event_name = 'response_{0}'.format(event.get_event_name())
        handled_event_host_id = event.get_target_host_id()
        handled_event_cluster_id = event.get_target_cluster_id()
        handled_event_hostgroup_id = event.get_target_hostgroup_id()

        logger.info('Send {0} event response, retcode: {1}'.format(event_name, retcode))

        resp_event = self.event_handler.create_event(event_name)
        resp_event.set_event_id(event_id)
        resp_event.set_response_code(retcode)
        resp_event.set_handled_event_id(handled_event_id)
        resp_event.set_handled_event_host_id(handled_event_host_id)
        resp_event.set_handled_event_cluster_id(handled_event_cluster_id)
        resp_event.set_handled_event_hostgroup_id(handled_event_hostgroup_id)

        self.channel_handler.wcache_handler.write(resp_event.to_json())

    def event_dispatch(self, event):
        """
        1310 等待
        1311 执行
        1312 超时
        1313 失败
        1314 成功
        1315 未知
        """
        retcode = 1315

        if not self.allow_dispatch(event):
            return
        self.event_response(event, retcode=1311)
        try:
            event_name = event.get_event_name()
            handler = self.engine_factory.create_handler(event_name)
            retcode = handler.dispose(event)
        except Exception as e:
            logger.error('Handle event: {0} with exception: {1}'.format(event, e.message))
        finally:
            self.event_response(event, retcode=retcode)

    def run(self):
        try:
            while not self._gsignal.is_set():
                need_wait = False
                events_data = self.event_get()
                if len(events_data) == 0:
                    need_wait = True
                    logger.info('No events ready, next scheduled at %s', self.next_scheduled)
                if len(_evnet_threads) > settings.ENGINE_MAX_THREADPOOL_SIZE:
                    need_wait = True
                    logger.info('To many threads, next scheduled at %s', self.next_scheduled)
                if need_wait is True:
                    time.sleep(settings.ENGINE_SCHEDULER_INTERVAL)
                    continue
                for event_data in events_data:
                    t = EventThread(event_data, self)
                    t.setDaemon(True)
                    t.start()
                    _evnet_threads.append(t)
                    # may be an  time-consuming task, so not join
                logger.info('Events ready, next scheduled at %s', self.next_scheduled)
                time.sleep(settings.ENGINE_SCHEDULER_INTERVAL)
            print 'Engine process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Engine process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Engine process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()

