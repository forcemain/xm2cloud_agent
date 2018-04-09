#! -*- coding: utf-8 -*-


class BaseMetaClass(type):
    subclass = []

    def __new__(cls, name, bases, attrs):
        klass = type.__new__(cls, name, bases, attrs)

        if name == 'BaseCollector':
            return klass
        if klass.enable is False:
            return klass
        if klass in BaseMetaClass.subclass:
            return klass
        BaseMetaClass.subclass.append(klass)

        return klass


class BaseCollector(object):
    __metaclass__ = BaseMetaClass

    loader = None
    enable = True

    def __iter__(self):
        for klass in BaseMetaClass.subclass:
            yield klass

    def get_metricdata(self, *args, **kwargs):
        raise NotImplementedError

    def start_collects(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def real_name(self):
        name = '{0}.{1}'.format(self.__module__, self.__class__.__name__)

        return name
