#! -*- coding: utf-8 -*-


import linux_metrics


from functools import partial
from agent.util.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Cpu(BaseMetric):
    def __init__(self, cpu_idle=None, cpu_user=None, cpu_iowait=None, cpu_system=None):
        self.cpu_idle = cpu_idle
        self.cpu_user = cpu_user
        self.cpu_iowait = cpu_iowait
        self.cpu_system = cpu_system

    def get_cpu_idle(self):
        return self.cpu_idle

    def set_cpu_idle(self, cpu_idle):
        self.cpu_idle = cpu_idle

    def get_cpu_user(self):
        return self.cpu_user

    def set_cpu_user(self, cpu_user):
        self.cpu_user = cpu_user

    def get_cpu_iowait(self):
        return self.cpu_iowait

    def set_cpu_iowait(self, cpu_iowait):
        self.cpu_iowait = cpu_iowait

    def get_cpu_system(self):
        return self.cpu_system

    def set_cpu_system(self, cpu_system):
        self.cpu_system = cpu_system

    def to_dict(self):
        data = {}
        if isinstance(self.get_cpu_idle(), MetricData):
            data['cpu_idle'] = self.get_cpu_idle().to_dict()
        if isinstance(self.get_cpu_user(), MetricData):
            data['cpu_user'] = self.get_cpu_user().to_dict()
        if isinstance(self.get_cpu_iowait(), MetricData):
            data['cpu_iowait'] = self.get_cpu_iowait().to_dict()
        if isinstance(self.get_cpu_system(), MetricData):
            data['cpu_system'] = self.get_cpu_system().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, cpu_usage, name):
        for case in Switch(name):
            if case('cpu_idle'):
                name = 'cpu.idle'
                value = cpu_usage.get('idle')

                return MetricData(name, value)
            if case('cpu_user'):
                name = 'cpu.user'
                value = cpu_usage.get('user')

                return MetricData(name, value)
            if case('cpu_iowait'):
                name = 'cpu.iowait'
                value = cpu_usage.get('iowait')

                return MetricData(name, value)
            if case('cpu_system'):
                name = 'cpu.system'
                value = cpu_usage.get('system')

                return MetricData(name, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        cpu_usage = linux_metrics.cpu_percents(sample_duration=1)
        data_func = partial(self.get_metricdata, cpu_usage)

        cpu_data = {
            'cpu_idle': data_func('cpu_idle'),
            'cpu_user': data_func('cpu_user'),
            'cpu_iowait': data_func('cpu_iowait'),
            'cpu_system': data_func('cpu_system')
        }
        instance = Cpu(**cpu_data)
        metrics.append(instance)

        return metrics
