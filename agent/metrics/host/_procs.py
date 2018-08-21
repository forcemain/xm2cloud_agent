#! -*- coding: utf-8 -*-


import linux_metrics


from functools import partial
from agent.common.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Process(BaseMetric):
    def __init__(self, procs_running=None):
        self.procs_running = procs_running

    def get_procs_running(self):
        return self.procs_running

    def set_procs_running(self, procs_running):
        self.procs_running = procs_running

    def to_dict(self):
        data = {}
        if isinstance(self.get_procs_running(), MetricData):
            data['procs_running'] = self.get_procs_running().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, name):
        tags = {}
        for case in Switch(name):
            if case('procs_running'):
                name = 'procs.running'
                value = linux_metrics.procs_running()

                return MetricData(name, tags, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        data_func = partial(self.get_metricdata)

        procs_data = {
            'procs_running': data_func('procs_running'),
        }
        instance = Process(**procs_data)
        metrics.append(instance)

        return metrics
