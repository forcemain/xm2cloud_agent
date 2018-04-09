#! -*- coding: utf-8 -*-


import time


from agent.util.enhance import Random
from agent.dao.userdata import UserDataDao
from agent.models.event.pub_event import PubEvent
from agent.models.event.event_type import EventType


class BaseEventHandler(object):
    def __init__(self, userdata_dao=None):
        self._userdata_dao = userdata_dao

    @property
    def userdata_dao(self):
        if isinstance(self._userdata_dao, UserDataDao):
            return self._userdata_dao
        self._userdata_dao = UserDataDao()

        return self._userdata_dao

    def encrypt_data(self, data):
        enc_method = None

        return enc_method, data

    def create_event(self, *args, **kwargs):
        raise NotImplementedError


class MonitorEventHandler(BaseEventHandler):
    def create_event(self, data):
        event = PubEvent()
        userdata = self.userdata_dao.get_user_data()

        event.set_event_uuid(Random.get_uuid())
        event.set_event_name(EventType.MONITORING)
        event.set_source_host_id(userdata.get_host_id())
        event.set_metric_uuid(userdata.get_metric_uuid())
        # get a millisecond timestamp
        event.set_event_timestamp(int(time.time()))
        event.set_source_cluster_id(userdata.get_cluster_id())
        event.set_source_hostgroup_id(userdata.get_hostgroup_id())

        # may be you want encrypt the data
        enc_method, event_data = self.encrypt_data(data)
        event.set_enc_method(enc_method)
        event.set_event_data(event_data)

        return event


class ChannelEventHandler(BaseEventHandler):
    def create_event(self, data):
        pass


class HeatbeatEventHandler(BaseEventHandler):
    def create_event(self, data):
        pass
