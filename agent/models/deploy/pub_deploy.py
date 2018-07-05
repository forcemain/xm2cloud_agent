#! -*- coding: utf-8 -*-


import json


from agent.models import BaseModel


class PubDeploy(BaseModel):
    def __init__(self, event=None, app_id=None, app_name=None, app_type=None, app_revision=None, revision_id=None,
                 download_url=None):
        self.event = event
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.revision_id = revision_id
        self.app_revision = app_revision
        self.download_url = download_url

    def get_event(self):
        return self.event

    def set_event(self, event):
        self.event = event

    def get_app_id(self):
        return self.app_id

    def set_app_id(self, app_id):
        self.app_id = app_id

    def get_app_name(self):
        return self.app_name

    def set_app_name(self, app_name):
        self.app_name = app_name

    def get_app_type(self):
        return self.app_type

    def set_app_type(self, app_type):
        self.app_type = app_type

    def get_revision_id(self):
        return self.revision_id

    def set_revision_id(self, revision_id):
        self.revision_id = revision_id

    def get_app_revision(self):
        return self.app_revision

    def set_app_revision(self, app_revision):
        self.app_revision = app_revision

    def get_download_url(self):
        return self.download_url

    def set_download_url(self, download_url):
        self.download_url = download_url

    def to_dict(self):
        data = {
            'event': self.get_event(),
            'app_id': self.get_app_id(),
            'app_name': self.get_app_name(),
            'app_type': self.get_app_type(),
            'revision_id': self.get_revision_id(),
            'app_revision': self.get_app_revision(),
            'download_url': self.get_download_url()
        }

        return data

    def is_valid(self):
        return True

    @staticmethod
    def from_dict(data):
        event = PubDeploy()
        map(lambda r: setattr(event, r[0], r[1]), data.iteritems())

        return event

    @staticmethod
    def from_json(data):
        dict_data = json.loads(data)
        event = PubDeploy.from_dict(dict_data)

        return event

