#! -*- coding: utf-8 -*-


import psutil


from functools import partial
from agent.common.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Mem(BaseMetric):
    def __init__(self, mem_memfree=None, mem_memused_percentage=None, mem_swapfree=None, mem_swapused_percentage=None):
        self.mem_memfree = mem_memfree
        self.mem_memused_percentage = mem_memused_percentage
        self.mem_swapfree = mem_swapfree
        self.mem_swapused_percentage = mem_swapused_percentage

    def get_mem_memfree(self):
        return self.mem_memfree

    def set_mem_memfree(self, mem_memfree):
        self.mem_memfree = mem_memfree

    def get_mem_memused_percentage(self):
        return self.mem_memused_percentage

    def set_mem_memused_percentage(self, mem_memused_percentage):
        self.mem_memused_percentage = mem_memused_percentage

    def get_mem_swapfree(self):
        return self.mem_swapfree

    def set_mem_swapfree(self, mem_swapfree):
        self.mem_swapfree = mem_swapfree

    def get_mem_swapused_percentage(self):
        return self.mem_swapused_percentage

    def set_mem_swapused_percentage(self, mem_swapused_percentage):
        self.mem_swapused_percentage = mem_swapused_percentage

    def to_dict(self):
        data = {}
        if isinstance(self.get_mem_memfree(), MetricData):
            data['mem_memfree'] = self.get_mem_memfree().to_dict()
        if isinstance(self.get_mem_memused_percentage(), MetricData):
            data['mem_memused_percentage'] = self.get_mem_memused_percentage().to_dict()
        if isinstance(self.get_mem_swapfree(), MetricData):
            data['mem_swapfree'] = self.get_mem_swapfree().to_dict()
        if isinstance(self.get_mem_swapused_percentage(), MetricData):
            data['mem_swapused_percentage'] = self.get_mem_swapused_percentage().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, mem_mem, mem_swap, name):
        tags = {}
        for case in Switch(name):
            if case('mem_memfree'):
                name = 'mem.memfree'
                value = mem_mem.free

                return MetricData(name, tags, value)
            if case('mem_memused_percentage'):
                name = 'mem.memused.percentage'
                value = mem_mem.percent

                return MetricData(name, tags, value)
            if case('mem_swapfree'):
                name = 'mem.swapfree'
                value = mem_swap.free

                return MetricData(name, tags, value)
            if case('mem_swapused_percentage'):
                name = 'mem.swapused.percentage'
                value = mem_swap.percent

                return MetricData(name, tags, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        memswap = psutil.swap_memory()
        memmem = psutil.virtual_memory()
        data_func = partial(self.get_metricdata, memmem, memswap)
        mem_data = {
            'mem_memfree': data_func('mem_memfree'),
            'mem_memused_percentage': data_func('mem_memused_percentage'),
            'mem_swapfree': data_func('mem_swapfree'),
            'mem_swapused_percentage': data_func('mem_swapused_percentage'),
        }
        instance = Mem(**mem_data)
        metrics.append(instance)

        return metrics
