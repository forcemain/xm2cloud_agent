#! -*- coding: utf-8 -*-


import os


from agent import database
from agent.common.logger import Logger
from agent.dao.userdata import UserDataDao
from agent.handler.cache import CacheHandler

logger = Logger.get_logger(__name__)


class BaseChannelHelper(object):
    def __init__(self, **kwargs):
        self._msg_sender = None
        self._msg_receiver = None
        self._rcache_handler = None
        self._wcache_handler = None
        self._ccache_handler = None
        self._ucache_handler = None
        self._dcache_handler = None
        self._dcache_path = kwargs.get('dcache_path', None)
        self._ucache_path = kwargs.get('ucache_path', None)
        self._ccache_path = kwargs.get('ccache_path', None)
        self._rcache_path = kwargs.get('rcache_path', None)
        self._wcache_path = kwargs.get('wcache_path', None)
        self._userdata_dao = kwargs.get('userdata_dao', None)

    @property
    def ccache_path(self):
        if self._ccache_path and os.path.exists(self._ccache_path):
            return self._ccache_path
        basedir = database.get_basedir()
        self._ccache_path = os.path.join(basedir, 'cache', 'channel', 'ccache')

        return self._ccache_path

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
    def ucache_path(self):
        if self._ucache_path and os.path.exists(self._ucache_path):
            return self._ucache_path
        basedir = database.get_basedir()
        self._ucache_path = os.path.join(basedir, 'cache', 'channel', 'ucache')

        return self._ucache_path

    @property
    def dcache_path(self):
        if self._dcache_path and os.path.exists(self._dcache_path):
            return self._dcache_path
        basedir = database.get_basedir()
        self._dcache_path = os.path.join(basedir, 'cache', 'channel', 'dcache')

        return self._dcache_path

    @property
    def ccache_handler(self):
        if isinstance(self._ccache_handler, CacheHandler):
            return self._ccache_handler
        self._ccache_handler = CacheHandler(cache_path=self.ccache_path)

        return self._ccache_handler

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
    def ucache_handler(self):
        if isinstance(self._ucache_handler, CacheHandler):
            return self._ucache_handler
        self._ucache_handler = CacheHandler(cache_path=self.ucache_path)

        return self._ucache_handler

    @property
    def dcache_handler(self):
        if isinstance(self._dcache_handler, CacheHandler):
            return self._dcache_handler
        self._dcache_handler = CacheHandler(cache_path=self.dcache_path)

        return self._ucache_handler

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
