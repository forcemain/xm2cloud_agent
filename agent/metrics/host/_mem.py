#! -*- coding: utf-8 -*-


import os
import json
import psutil


from functools import partial
from agent.util.enhance import Switch
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Mem(object):
    def __init__(self, mem_memtotal=None, mem_memused=None, mem_memfree=None, mem_memused_percentage=None,
                 mem_swaptotal=None, mem_swapused=None, mem_swapfree=None, mem_swapused_percentage=None):
        self.mem_memtotal = mem_memtotal
        self.mem_memused = mem_memused
        self.mem_memfree = mem_memfree
        self.mem_memused_percentage = mem_memused_percentage
        self.mem_swaptotal = mem_swaptotal
        self.mem_swapused = mem_swapused
        self.mem_swapfree = mem_swapfree
        self.mem_swapused_percentage = mem_swapused_percentage

    def get_mem_memtotal(self):
        return self.mem_memtotal

    def set_mem_memtotal(self, mem_memtotal):
        self.mem_memtotal = mem_memtotal

    def get_mem_memused(self):
        return self.mem_memused

    def set_mem_memused(self, mem_memused):
        self.mem_memused = mem_memused

    def get_mem_memfree(self):
        return self.mem_memfree

    def set_mem_memfree(self, mem_memfree):
        self.mem_memfree = mem_memfree

    def get_mem_memused_percentage(self):
        return self.mem_memused_percentage

    def set_mem_memused_percentage(self, mem_memused_percentage):
        self.mem_memused_percentage = mem_memused_percentage

    def get_mem_swaptotal(self):
        return self.mem_swaptotal

    def set_mem_swaptotal(self, mem_swaptotal):
        self.mem_swaptotal = mem_swaptotal

    def get_mem_swapused(self):
        return self.mem_swapused

    def set_mem_swapused(self, mem_swapused):
        self.mem_swapused = mem_swapused

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
        if isinstance(self.get_mem_memtotal(), MetricData):
            data['mem_memtotal'] = self.get_mem_memtotal().to_dict()
        if isinstance(self.get_mem_memused(), MetricData):
            data['mem_memused'] = self.get_mem_memused().to_dict()
        if isinstance(self.get_mem_memfree(), MetricData):
            data['mem_memfree'] = self.get_mem_memfree().to_dict()
        if isinstance(self.get_mem_memused_percentage(), MetricData):
            data['mem_memused_percentage'] = self.get_mem_memused_percentage().to_dict()
        if isinstance(self.get_mem_swaptotal(), MetricData):
            data['mem_swaptotal'] = self.get_mem_swaptotal().to_dict()
        if isinstance(self.get_mem_swapused(), MetricData):
            data['mem_swapused'] = self.get_mem_swapused().to_dict()
        if isinstance(self.get_mem_swapfree(), MetricData):
            data['mem_swapfree'] = self.get_mem_swapfree().to_dict()
        if isinstance(self.get_mem_swapused_percentage(), MetricData):
            data['mem_swapused_percentage'] = self.get_mem_swapused_percentage().to_dict()

        return data

    def to_json(self, indent=4):
        dict_data = self.to_dict()
        json_data = json.dumps(dict_data, indent=indent)

        return json_data

    def __str__(self):
        desc = '<{0}: {1}{2}>'.format(__name__, os.linesep, self.to_json(indent=4))

        return desc


class Collector(BaseCollector):
    def get_metricdata(self, mem_mem, mem_swap, name):
        for case in Switch(name):
            if case('mem_memtotal'):
                name = 'mem.memtotal'
                value = mem_mem.total

                return MetricData(name, value)
            if case('mem_memused'):
                name = 'mem.memused'
                value = mem_mem.used

                return MetricData(name, value)
            if case('mem_memfree'):
                name = 'mem.memfree'
                value = mem_mem.free

                return MetricData(name, value)
            if case('mem_memused_percentage'):
                name = 'mem.memused.percentage'
                value = mem_mem.percent

                return MetricData(name, value)
            if case('mem_swaptotal'):
                name = 'mem.swaptotal'
                value = mem_swap.total

                return MetricData(name, value)
            if case('mem_swapused'):
                name = 'mem.swapused'
                value = mem_swap.used

                return MetricData(name, value)
            if case('mem_swapfree'):
                name = 'mem.swapfree'
                value = mem_swap.free

                return MetricData(name, value)
            if case('mem_swapused_percentage'):
                name = 'mem.swapused.percentage'
                value = mem_swap.percent

                return MetricData(name, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        memswap = psutil.swap_memory()
        memmem = psutil.virtual_memory()
        data_func = partial(self.get_metricdata, memmem, memswap)
        mem_data = {
            'mem_memtotal': data_func('mem_memtotal'),
            'mem_memused': data_func('mem_memused'),
            'mem_memfree': data_func('mem_memfree'),
            'mem_memused_percentage': data_func('mem_memused_percentage'),
            'mem_swaptotal': data_func('mem_swaptotal'),
            'mem_swapused': data_func('mem_swapused'),
            'mem_swapfree': data_func('mem_swapfree'),
            'mem_swapused_percentage': data_func('mem_swapused_percentage'),
        }
        instance = Mem(**mem_data)
        metrics.append(instance)

        return metrics
