#! -*- coding: utf-8 -*-


from agent.common.logger import Logger
from agent.handler.event.logging import LoggingEventHandler
from agent.handler.channel.rabbitmq import RabbitMQChannelHandler


logger = Logger.get_logger(__name__)


class BaseMetaClass(type):
    subclass = {}

    def __new__(cls, name, bases, attrs):
        klass = type.__new__(cls, name, bases, attrs)

        if name == 'BaseEngineHandler':
            return klass
        if klass.enable is False:
            return klass

        BaseMetaClass.subclass.update({klass.name: klass})

        return klass


class BaseEngineHandler(object):
    __metaclass__ = BaseMetaClass

    name = None
    enable = True

    def __init__(self, event_handler=None, channel_handler=None):
        self._event_handler = event_handler
        self._channel_handler = channel_handler

    @property
    def real_name(self):
        name = '{0}.{1}'.format(self.__module__, self.__class__.__name__)

        return name

    @property
    def event_handler(self):
        if isinstance(self._event_handler, LoggingEventHandler):
            return self._event_handler
        self._event_handler = LoggingEventHandler()

        return self._event_handler

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    def async_logging(self, levelname, event, message):
        message = message.strip()
        if not message:
            return
        event_id = event.get_event_id()
        if levelname == 'INFO':
            logger.info('Event {0} stdout: {1}'.format(event_id, message))
        if levelname == 'ERROR':
            logger.error('Event {0} stderr: {1}'.format(event_id, message))

        logging_event = self.event_handler.create_event(levelname, message)
        logging_event.set_event_id(event_id)

        self.channel_handler.wcache_handler.write(logging_event.to_json())

    def info(self, event, message):
        self.async_logging('INFO', event, message)

    def error(self, event, message):
        self.async_logging('ERROR', event, message)

    def is_local_event(self, event):
        userdata = self.channel_handler.userdata_dao.get_user_data()

        local_host_id = userdata.get_host_id()
        event_host_id = event.get_source_host_id()

        return event_host_id == local_host_id

    def dispose_notexists(self, event):
        event_name = event.get_event_name()
        message = 'No engine handler handle event: {0}'.format(event_name)

        logger.warning(message)
        self.async_logging('WARN', event, message)

    def dispose_exception(self, event, message):
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        if self.is_local_event(event):
            _message = 'Handle local event: {0} with exception: {1}'.format(event, message)
        else:
            _message = 'Hanlde  outer event: {0} (host: {1}, hostgroup: {1}, cluster: {2}) with exception: {3}'.format(
                event, target_host_id, target_hostgroup_id, target_cluster_id, message
            )
        logger.error(_message)
        self.async_logging('ERROR', event, message)

    def before_dispose(self, event):
        event_name = event.get_event_name()
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        if self.is_local_event(event):
            message = 'Start handle local event: {0}'.format(event_name)
        else:
            message = 'Start handle outer event: {0} (host: {1}, hostgroup: {1}, cluster: {2})'.format(
                event_name, target_host_id, target_hostgroup_id, target_cluster_id
            )
        logger.info(message)
        self.async_logging('INFO', event, message)

    def after_dispose(self, event):
        event_name = event.get_event_name()
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        if self.is_local_event(event):
            message = 'Finish handle local event: {0}'.format(event_name)
        else:
            message = 'Finish handle outer event: {0} (host: {1}, hostgroup: {1}, cluster: {2})'.format(
                event_name, target_host_id, target_hostgroup_id, target_cluster_id
            )
        logger.info(message)
        self.async_logging('INFO', event, message)

    def handle(self, event):
        raise NotImplementedError

    def dispose(self, event):
        self.before_dispose(event)
        try:
            self.handle(event)
        except Exception as e:
            self.dispose_exception(event, e)
            logger.error('{0} handle event: {1} with error: {2}'.format(self.real_name, event, e))
        finally:
            self.after_dispose(event)


class EngineHandlerFactory(object):
    def create_handler(self, name):
        name = name if name in BaseMetaClass.subclass else 'default'
        klss = BaseMetaClass.subclass.get(name)

        return klss()
