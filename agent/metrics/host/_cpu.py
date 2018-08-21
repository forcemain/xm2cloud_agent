#! -*- coding: utf-8 -*-


import linux_metrics


from functools import partial
from agent.common.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Cpu(BaseMetric):
    def __init__(self, cpu_used_percentage=None):
        self.cpu_used_percentage = cpu_used_percentage

    def get_cpu_used_percentage(self):
        return self.cpu_used_percentage

    def set_cpu_used_percentage(self, cpu_used_percentage):
        self.cpu_used_percentage = cpu_used_percentage

    def to_dict(self):
        data = {}
        if isinstance(self.get_cpu_used_percentage(), MetricData):
            data['cpu_used_percentage'] = self.get_cpu_used_percentage().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, cpu_usage, name):
        tags = {}
        for case in Switch(name):
            if case('cpu_used_percentage'):
                name = 'cpu.used.percentage'
                value = 100 - cpu_usage.get('idle')

                return MetricData(name, tags, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        cpu_usage = linux_metrics.cpu_percents(sample_duration=1)
        data_func = partial(self.get_metricdata, cpu_usage)

        cpu_data = {
            'cpu_used_percentage': data_func('cpu_used_percentage'),
        }
        instance = Cpu(**cpu_data)
        metrics.append(instance)

        return metrics
