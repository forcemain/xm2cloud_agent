#! -*- coding: utf-8 -*-


class BaseMetaClass(type):
    subclass = []

    def __new__(cls, name, bases, attrs):
        klass = type.__new__(cls, name, bases, attrs)

        if name != 'BaseCollector' and klass not in BaseMetaClass.subclass:
            BaseMetaClass.subclass.append(klass)

        return klass


class BaseCollector(object):
    __metaclass__ = BaseMetaClass

    loader = None

    def __iter__(self):
        for klass in BaseMetaClass.subclass:
            yield klass

    def get_metricdata(self, *args, **kwargs):
        raise NotImplementedError

    def start_collects(self, *args, **kwargs):
        raise NotImplementedError

