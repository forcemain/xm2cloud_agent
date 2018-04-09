#! -*- coding: utf-8 -*-


import json


from agent.models import BaseModel
from agent import get_name, get_version


class PubEvent(BaseModel):
    def __init__(self, event_uuid=None, event_id=None, chain_event_id=None, event_name=None, event_source=get_name(),
                 source_version=get_version(), source_cluster_id=None, source_hostgroup_id=None, source_host_id=None,
                 target_cluster_id=None, target_hostgroup_id=None, target_host_id=None, handled_event_id=None,
                 handled_event_cluster_id=None, handled_event_hostgroup_id=None, handled_event_host_id=None,
                 event_timestamp=None, event_data=None, enc_method=None, metric_uuid=None):

        self.event_id = event_id
        self.event_data = event_data
        self.event_name = event_name
        self.event_uuid = event_uuid
        self.enc_method = enc_method
        self.metric_uuid = metric_uuid
        self.event_source = event_source
        self.target_host_id = target_host_id
        self.source_version = source_version
        self.chain_event_id = chain_event_id
        self.source_host_id = source_host_id
        self.event_timestamp = event_timestamp
        self.handled_event_id = handled_event_id
        self.target_cluster_id = target_cluster_id
        self.source_cluster_id = source_cluster_id
        self.target_hostgroup_id = target_hostgroup_id
        self.source_hostgroup_id = source_hostgroup_id
        self.handled_event_host_id = handled_event_host_id
        self.handled_event_cluster_id = handled_event_cluster_id
        self.handled_event_hostgroup_id = handled_event_hostgroup_id

    def get_event_id(self):
        return self.event_id

    def set_event_id(self, event_id):
        self.event_id = event_id

    def get_metric_uuid(self):
        return self.metric_uuid

    def set_metric_uuid(self, metric_uuid):
        self.metric_uuid = metric_uuid

    def get_enc_method(self):
        return self.enc_method

    def set_enc_method(self, enc_method):
        self.enc_method = enc_method

    def get_event_data(self):
        return self.event_data

    def set_event_data(self, event_data):
        self.event_data = event_data

    def get_event_name(self):
        return self.event_name

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_uuid(self):
        return self.event_uuid

    def set_event_uuid(self, event_uuid):
        self.event_uuid = event_uuid

    def get_event_source(self):
        return self.event_source

    def set_event_source(self, event_source):
        self.event_source = event_source

    def get_target_host_id(self):
        return self.target_host_id

    def set_target_host_id(self, target_host_id):
        self.target_host_id = target_host_id

    def get_source_version(self):
        return self.source_version

    def set_source_version(self, source_version):
        self.source_version = source_version

    def get_chain_event_id(self):
        return self.chain_event_id

    def set_chain_event_id(self, chain_event_id):
        self.chain_event_id = chain_event_id

    def get_source_host_id(self):
        return self.source_host_id

    def set_source_host_id(self, source_host_id):
        self.source_host_id = source_host_id

    def get_event_timestamp(self):
        return self.event_timestamp

    def set_event_timestamp(self, event_timestamp):
        self.event_timestamp = event_timestamp

    def get_handled_event_id(self):
        return self.handled_event_id

    def set_handled_event_id(self, handled_event_id):
        self.handled_event_id = handled_event_id

    def get_target_cluster_id(self):
        return self.target_cluster_id

    def set_target_cluster_id(self, target_cluster_id):
        self.target_cluster_id = target_cluster_id

    def get_source_cluster_id(self):
        return self.source_cluster_id

    def set_source_cluster_id(self, source_cluster_id):
        self.source_cluster_id = source_cluster_id

    def get_target_hostgroup_id(self):
        return self.target_hostgroup_id

    def set_target_hostgroup_id(self, target_hostgroup_id):
        self.target_hostgroup_id = target_hostgroup_id

    def get_source_hostgroup_id(self):
        return self.source_hostgroup_id

    def set_source_hostgroup_id(self, source_hostgroup_id):
        self.source_hostgroup_id = source_hostgroup_id

    def get_handled_event_host_id(self):
        return self.handled_event_host_id

    def set_handled_event_host_id(self, handled_event_host_id):
        self.handled_event_host_id = handled_event_host_id

    def get_handled_event_cluster_id(self):
        return self.handled_event_cluster_id

    def set_handled_event_cluster_id(self, handled_event_cluster_id):
        self.handled_event_cluster_id = handled_event_cluster_id

    def get_handled_event_hostgroup_id(self):
        return self.handled_event_hostgroup_id

    def set_handled_event_hostgroup_id(self, handled_event_hostgroup_id):
        self.handled_event_hostgroup_id = handled_event_hostgroup_id

    def to_dict(self):
        data = {
            'event_id': self.get_event_id(),
            'event_data': self.get_event_data(),
            'event_name': self.get_event_name(),
            'enc_method': self.get_enc_method(),
            'event_uuid': self.get_event_uuid(),
            'metric_uuid': self.get_metric_uuid(),
            'event_source': self.get_event_source(),
            'target_host_id': self.get_target_host_id(),
            'source_version': self.get_source_version(),
            'chain_event_id': self.get_chain_event_id(),
            'source_host_id': self.get_source_host_id(),
            'event_timestamp': self.get_event_timestamp(),
            'handled_event_id': self.get_handled_event_id(),
            'target_cluster_id': self.get_target_cluster_id(),
            'source_cluster_id': self.get_source_cluster_id(),
            'target_hostgroup_id': self.get_target_hostgroup_id(),
            'source_hostgroup_id': self.get_source_hostgroup_id(),
            'handled_event_host_id': self.get_handled_event_host_id(),
            'handled_event_cluster_id': self.get_handled_event_cluster_id(),
            'handled_event_hostgroup_id': self.get_handled_event_hostgroup_id()
        }

        return data

    def is_valid(self):
        return True

    @staticmethod
    def from_dict(data):
        allfields = [
            'event_uuid', 'event_id', 'chain_event_id', 'event_name', 'event_source', 'source_version',
            'source_cluster_id', 'source_hostgroup_id', 'source_host_id', 'target_cluster_id', 'target_hostgroup_id',
            'target_host_id', 'handled_event_id', 'handled_event_cluster_id', 'handled_event_hostgroup_id',
            'handled_event_host_id', 'event_timestamp', 'event_data', 'enc_method', 'metric_uuid'
        ]
        allvalues = map(lambda k: data.get(k, None), allfields)

        event = PubEvent(**dict(zip(allfields, allvalues)))

        return event

    @staticmethod
    def from_json(data):
        dict_data = json.loads(data)
        event = PubEvent.from_dict(dict_data)

        return event
