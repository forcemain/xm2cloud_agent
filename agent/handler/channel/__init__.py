#! -*- coding: utf-8 -*-


import os


from agent import database
from agent.util.logger import Logger
from agent.dao.userdata import UserDataDao
from agent.handler.cache import CacheHandler

logger = Logger.get_logger(__name__)


class BaseChannelHelper(object):
    def __init__(self, **kwargs):
        self._msg_sender = None
        self._msg_receiver = None
        self._rcache_handler = None
        self._wcache_handler = None
        self._rcache_path = kwargs.get('rcache_path', None)
        self._wcache_path = kwargs.get('wcache_path', None)
        self._userdata_dao = kwargs.get('userdata_dao', None)

    @property
    def rcache_path(self):
        if self._rcache_path and os.path.exists(self._rcache_path):
            return self._rcache_path
        basedir = database.get_basedir()
        self._rcache_path = os.path.join(basedir, 'cache', 'channel', 'rcache')

        return self._rcache_path

    @property
    def wcache_path(self):
        if self._wcache_path and os.path.exists(self._wcache_path):
            return self._wcache_path
        basedir = database.get_basedir()
        self._wcache_path = os.path.join(basedir, 'cache', 'channel', 'wcache')

        return self._wcache_path

    @property
    def rcache_handler(self):
        if isinstance(self._rcache_handler, CacheHandler):
            return self._rcache_handler
        self._rcache_handler = CacheHandler(cache_path=self.rcache_path)

        return self._rcache_handler

    @property
    def wcache_handler(self):
        if isinstance(self._wcache_handler, CacheHandler):
            return self._wcache_handler
        self._wcache_handler = CacheHandler(cache_path=self.wcache_path)

        return self._wcache_handler

    @property
    def userdata_dao(self):
        if isinstance(self._userdata_dao, UserDataDao):
            return self._userdata_dao
        self._userdata_dao = UserDataDao()

        return self._userdata_dao


class BaseChannelHandler(object):
    def __init__(self, **kwargs):
        self._msg_sender = kwargs.get('msg_sender', None)
        self._msg_receiver = kwargs.get('msg_receiver', None)

    @property
    def msg_sender(self):
        raise NotImplementedError

    @property
    def msg_receiver(self):
        raise NotImplementedError
