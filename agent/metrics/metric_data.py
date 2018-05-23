#! -*- coding: utf-8 -*-


import json


class MetricData(object):
    def __init__(self, name=None, tags=None, value=None):
        self.name = name
        self.tags = tags
        self.value = value

    def __str__(self):
        return self.to_json()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def to_dict(self):
        data = {
            'name': self.get_name(),
            'tags': self.get_tags(),
            'value': self.get_value()
        }

        return data

    def to_json(self, indent=4):
        dict_data = self.to_dict()

        json_data = json.dumps(dict_data, indent=indent)

        return json_data

    @staticmethod
    def from_dict(data):
        metric = MetricData()
        map(lambda r: setattr(metric, r[0], r[1]), data.iteritems())

        return metric

    @staticmethod
    def from_json(data):
        dict_data = json.loads(data)
        metric = MetricData.from_dict(dict_data)

        return metric

