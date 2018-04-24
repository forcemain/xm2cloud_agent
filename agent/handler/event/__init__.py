#! -*- coding: utf-8 -*-


from agent.dao.userdata import UserDataDao


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
        encryption = None

        return encryption, data

    def create_event(self, *args, **kwargs):
        raise NotImplementedError
