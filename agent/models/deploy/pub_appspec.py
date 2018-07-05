#! -*- coding: utf-8 -*-


import json


from agent.models import BaseModel


class PubAppSpec(BaseModel):
    def __init__(self, version=None, os=None, files=None, hooks=None):
        self.version = version
        self.os = os
        self.files = files
        self.hooks = hooks

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version

    def get_os(self):
        return self.os

    def set_os(self, os):
        self.os = os

    def get_files(self):
        return self.files

    def set_files(self, files):
        self.files = files

    def get_hooks(self):
        return self.hooks

    def set_hooks(self, hooks):
        self.hooks = hooks

    def to_dict(self):
        data = {
            'version': self.get_version(),
            'os': self.get_os(),
            'files': self.get_files(),
            'hooks': self.get_hooks(),
        }

        return data

    def is_valid(self):
        return True

    @staticmethod
    def from_dict(data):
        event = PubAppSpec()
        map(lambda r: setattr(event, r[0], r[1]), data.iteritems())

        return event

    @staticmethod
    def from_json(data):
        dict_data = json.loads(data)
        event = PubAppSpec.from_dict(dict_data)

        return event

