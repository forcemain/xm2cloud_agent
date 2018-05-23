#! -*- coding: utf-8 -*-


import time


from agent.common.enhance import Random
from agent.handler.event import BaseEventHandler
from agent.models.event.pub_event import PubEvent
from agent.models.event.event_type import EventType


class MonitorEventHandler(BaseEventHandler):
    def create_event(self, data):
        event = PubEvent()
        userdata = self.userdata_dao.get_user_data()

        event.set_event_uuid(Random.get_uuid())
        event.set_event_name(EventType.MONITORING)
        event.set_source_host_id(userdata.get_host_id())
        event.set_event_timestamp(int(time.time()))
        event.set_source_cluster_id(userdata.get_cluster_id())
        event.set_source_hostgroup_id(userdata.get_hostgroup_id())

        # may be you want encrypt the data
        encryption, event_data = self.encrypt_data(data)
        event.set_encryption(encryption)
        event.set_event_data(event_data)

        return event
