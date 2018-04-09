#! -*- coding: utf-8 -*-


import linux_metrics


from functools import partial
from agent.util.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Load(BaseMetric):
    def __init__(self, load_1min=None, load_5min=None, load_15min=None):
        self.load_1min = load_1min
        self.load_5min = load_5min
        self.load_15min = load_15min

    def get_load_1min(self):
        return self.load_1min

    def set_load_1min(self, load_1min):
        self.load_1min = load_1min

    def get_load_5min(self):
        return self.load_5min

    def set_load_5min(self, load_5min):
        self.load_5min = load_5min

    def get_load_15min(self):
        return self.load_15min

    def set_load_15min(self, load_15min):
        self.load_15min = load_15min

    def to_dict(self):
        data = {}
        if isinstance(self.get_load_1min(), MetricData):
            data['load_1min'] = self.get_load_1min().to_dict()
        if isinstance(self.get_load_5min(), MetricData):
            data['load_5min'] = self.get_load_5min().to_dict()
        if isinstance(self.get_load_15min(), MetricData):
            data['load_15min'] = self.get_load_15min().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, load_usage, name):
        for case in Switch(name):
            if case('load_1min'):
                name = 'load.1min'
                value = load_usage[0]

                return MetricData(name, value)
            if case('load_5min'):
                name = 'load.5min'
                value = load_usage[1]

                return MetricData(name, value)
            if case('load_15min'):
                name = 'load.15min'
                value = load_usage[2]

                return MetricData(name, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        load_usage = linux_metrics.load_avg()
        data_func = partial(self.get_metricdata, load_usage)
        load_data = {
            'load_1min': data_func('load_1min'),
            'load_5min': data_func('load_5min'),
            'load_15min': data_func('load_15min')
        }
        instance = Load(**load_data)
        metrics.append(instance)

        return metrics
