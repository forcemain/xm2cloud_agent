#! -*- coding: utf-8 -*-


import time


from agent.common.enhance import Random
from agent.handler.event import BaseEventHandler
from agent.models.event.pub_event import PubEvent


class EngineEventHandler(BaseEventHandler):
    def create_event(self, name):
        event = PubEvent()
        userdata = self.userdata_dao.get_user_data()

        event.set_event_name(name)
        event.set_event_uuid(Random.get_uuid())
        event.set_event_timestamp(int(time.time()))
        event.set_source_host_id(userdata.get_host_id())
        event.set_source_cluster_id(userdata.get_cluster_id())
        event.set_source_hostgroup_id(userdata.get_hostgroup_id())

        return event
