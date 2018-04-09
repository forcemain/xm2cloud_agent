#! -*- coding: utf-8 -*-


import os
import json


class BaseModel(object):
    def to_dict(self):
        raise NotImplementedError

    def to_json(self, indent=4):
        dict_data = self.to_dict()
        json_data = json.dumps(dict_data, indent=indent)

        return json_data

    def is_valid(self):
        raise NotImplementedError

    @staticmethod
    def from_dict(data):
        pass

    @staticmethod
    def from_json(data):
        pass

    def __str__(self):
        desc = '<{0}: {1}{2}>'.format(__name__, os.linesep, self.to_json(indent=4))

        return desc
