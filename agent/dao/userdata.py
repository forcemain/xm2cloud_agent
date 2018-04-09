#! -*- coding: utf-8 -*-


import os

from agent import settings
from agent.util.enhance import File
from agent.models.userdata.user_data import UserData


class UserDataDao(object):
    def __init__(self, udata_path=None):
        self._udata_path = udata_path

    @property
    def udata_path(self):
        if self._udata_path and os.path.exists(self._udata_path):
            return self._udata_path
        self._udata_path = settings.DEFAULT_USERDATA_PATH

        return self._udata_path

    def get_json_data(self):
        json_data = File.read_content(self.udata_path)

        return json_data

    def get_user_data(self):
        json_data = self.get_json_data()
        user_data = UserData.from_json(json_data)

        return user_data

