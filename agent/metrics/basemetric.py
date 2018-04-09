#! -*- coding: utf-8 -*-


import os
import json


class BaseMetric(object):
    def to_dict(self):
        raise NotImplementedError

    def to_json(self, indent=4):
        dict_data = self.to_dict()
        json_data = json.dumps(dict_data, indent=indent)

        return json_data

    def is_valid(self):
        raise NotImplementedError

    @property
    def real_name(self):
        name = '{0}.{1}'.format(self.__module__, self.__class__.__name__)

        return name

    def __str__(self):
        desc = '<{0}: {1}{2}>'.format(self.real_name, os.linesep, self.to_json(indent=4))

        return desc
