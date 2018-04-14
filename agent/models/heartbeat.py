#! -*- coding: utf-8 -*-


import json

from agent.models import BaseModel
from agent import get_name, get_version


class Heartbeat(BaseModel):
    def __init__(self, name=None, version=None):
        self.name = name or get_name()
        self.version = version or get_version()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version

    def is_valid(self):
        return True

    def to_dict(self):
        data = {
            'name': self.get_name(),
            'version': self.get_version()
        }

        return data

    @staticmethod
    def from_dict(data):
        allfields = ['name', 'version']
        allvalues = map(lambda k: data.get(k, None), allfields)

        event = Heartbeat(**dict(zip(allfields, allvalues)))

        return event

    @staticmethod
    def from_json(data):
        dict_data = json.loads(data)
        event = Heartbeat.from_dict(dict_data)

        return event




