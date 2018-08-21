#! -*- coding: utf-8 -*-


import pika


from agent import settings
from agent.common.logger import Logger
from agent.common.amqp.sender import AMQPSender
from agent.models.event.pub_event import PubEvent
from agent.common.amqp.receiver import AMQPReceiver
from agent.handler.channel import BaseChannelHelper, BaseChannelHandler


logger = Logger.get_logger(__name__)


class RabbitMQChannelSender(BaseChannelHelper, AMQPSender):
    def __init__(self, **kwargs):
        AMQPSender.__init__(self, **kwargs)
        BaseChannelHelper.__init__(self, **kwargs)

        self._userdata = self.userdata_dao.get_user_data()

        self._ssl = self._userdata.get_rabbitmq_ssl()
        self._host = self._userdata.get_rabbitmq_host()
        self._port = self._userdata.get_rabbitmq_port()
        self._vhost = self._userdata.get_rabbitmq_vhost()
        self._auth_user = self._userdata.get_rabbitmq_auth_user()
        self._auth_pass = self._userdata.get_rabbitmq_auth_pass()
        self._exchange = self._userdata.get_rabbitmq_up_exchange()
        self._routing_key = self._userdata.get_rabbitmq_up_routing_key()

    def connect(self):
        conn_parameters = pika.ConnectionParameters(
            heartbeat=15,
            retry_delay=5,
            ssl=self._ssl,
            host=self._host,
            port=self._port,
            channel_max=1000,
            socket_timeout=15,
            connection_attempts=5,
            virtual_host=self._vhost,
            credentials=pika.PlainCredentials(self._auth_user, self._auth_pass)
        )

        logger.info('Connecting to {0}:{1}'.format(self._host, self._port))
        return pika.SelectConnection(conn_parameters,
                                     self.on_connection_open,
                                     stop_ioloop_on_close=True)

    def allow_send(self, fcontent):
        event = PubEvent.from_json(fcontent)

        return event.is_valid()

    def publish_message(self):
        if self._stopping:
            return
        # default batch 50, can be set larger
        events_data = self.wcache_handler.read(batch=settings.CHANNEL_SENDER_EVENT_BATCH_SIZE)
        for fname, fcontent in events_data:
            self.wcache_handler.remove(fname)
            if not self.allow_send(fcontent):
                logger.warning('Not allowed send this event data: {0}'.format(fcontent))
                continue
            # fpath = os.path.join(self.wcache_handler.cache_path, fname)
            self._channel.basic_publish(self._exchange, self._routing_key, fcontent, properties={})
        self.schedule_next_message()


class RabbitMQChannelReceiver(BaseChannelHelper, AMQPReceiver):
    def __init__(self, **kwargs):
        AMQPReceiver.__init__(self, **kwargs)
        BaseChannelHelper.__init__(self, **kwargs)

        self._userdata = self.userdata_dao.get_user_data()

        self._ssl = self._userdata.get_rabbitmq_ssl()
        self._host = self._userdata.get_rabbitmq_host()
        self._port = self._userdata.get_rabbitmq_port()
        self._vhost = self._userdata.get_rabbitmq_vhost()
        self._auth_user = self._userdata.get_rabbitmq_auth_user()
        self._auth_pass = self._userdata.get_rabbitmq_auth_pass()
        self._exchange = self._userdata.get_rabbitmq_down_exchange()
        self._routing_key = self._userdata.get_rabbitmq_down_routing_key()
        self._exchange_type = self._userdata.get_rabbitmq_down_exchange_type()

    def connect(self):
        conn_parameters = pika.ConnectionParameters(
            heartbeat=15,
            retry_delay=5,
            ssl=self._ssl,
            host=self._host,
            port=self._port,
            channel_max=1000,
            socket_timeout=15,
            connection_attempts=5,
            virtual_host=self._vhost,
            credentials=pika.PlainCredentials(self._auth_user, self._auth_pass)
        )

        logger.info('Connecting to {0}:{1}'.format(self._host, self._port))
        return pika.SelectConnection(conn_parameters,
                                     self.on_connection_open,
                                     stop_ioloop_on_close=True)

    def allow_receive(self, fcontent):
        # reload user data, prevent user data update
        self._userdata = self.userdata_dao.get_user_data()

        # get source from userdata event
        host_id = self._userdata.get_host_id()
        cluster_id = self._userdata.get_cluster_id()
        hostgroup_id = self._userdata.get_hostgroup_id()

        # get target_... from server event
        event = PubEvent.from_json(fcontent)
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        # is it my task ?
        if isinstance(target_host_id, list) and target_host_id:
            return host_id in target_host_id
        elif isinstance(target_hostgroup_id, list) and target_hostgroup_id:
            return isinstance(hostgroup_id, list) and (set(target_hostgroup_id) & set(hostgroup_id))
        elif isinstance(target_cluster_id, list) and target_cluster_id:
            return isinstance(cluster_id, list) and (set(target_cluster_id) & set(cluster_id))
        return False

    def on_message(self, unused_channel, basic_deliver, properties, body):
        logger.info('Received message # %s from %s: %s',
                    basic_deliver.delivery_tag, properties.app_id, body)
        if not self.allow_receive(body):
            logger.warning('Not allowed receive this event data: {0}'.format(body))
            return
        # put it to local cache
        self.rcache_handler.write(body)


class RabbitMQChannelHandler(BaseChannelHelper, BaseChannelHandler):
    def __init__(self, **kwargs):
        BaseChannelHelper.__init__(self, **kwargs)
        BaseChannelHandler.__init__(self, **kwargs)

    @property
    def msg_receiver(self):
        if isinstance(self._msg_receiver, AMQPReceiver):
            return self._msg_receiver
        self._msg_receiver = RabbitMQChannelReceiver()

        return self._msg_receiver

    @property
    def msg_sender(self):
        if isinstance(self._msg_sender, AMQPSender):
            return self._msg_sender
        self._msg_sender = RabbitMQChannelSender()

        return self._msg_sender
