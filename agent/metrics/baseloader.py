#! -*- coding: utf-8 -*-


class BaseLoader(object):
    @property
    def init_conf(self):
        raise NotImplementedError

    @property
    def inst_conf(self):
        raise NotImplementedError

    @property
    def inst_with_tags(self):
        raise NotImplementedError
