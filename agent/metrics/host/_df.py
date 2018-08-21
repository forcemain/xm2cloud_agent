#! -*- coding: utf-8 -*-


import os
import psutil


from functools import partial
from agent.common.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Df(BaseMetric):
    def __init__(self, df_bytes_free=None, df_bytes_used_percentage=None):
        self.df_bytes_free = df_bytes_free
        self.df_bytes_used_percentage = df_bytes_used_percentage

    def get_df_bytes_free(self):
        return self. df_bytes_free

    def set_df_bytes_free(self, df_bytes_free):
        self.df_bytes_free = df_bytes_free

    def get_df_bytes_used_percentage(self):
        return self.df_bytes_used_percentage

    def set_df_bytes_used_percentage(self, df_bytes_used_percentage):
        self.df_bytes_used_percentage = df_bytes_used_percentage

    def to_dict(self):
        data = {}
        if isinstance(self.get_df_bytes_free(), MetricData):
            data['df_bytes_free'] = self.get_df_bytes_free().to_dict()
        if isinstance(self.get_df_bytes_used_percentage(), MetricData):
            data['df_bytes_used_percentage'] = self.get_df_bytes_used_percentage().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, disk, disk_usage, name):
        tags = {'mount': disk.mountpoint}
        for case in Switch(name):
            if case('df_bytes_free'):
                name = 'df.bytes.free'
                value = disk_usage.free

                return MetricData(name, tags, value)
            if case('df_bytes_used_percentage'):
                name = 'df.bytes.used.percentage'
                value = disk_usage.percent

                return MetricData(name, tags, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        disk_partitions = psutil.disk_partitions(all=False)
        if not disk_partitions:
            return metrics

        for disk in disk_partitions:
            disk_usage = psutil.disk_usage(disk.mountpoint)
            data_func = partial(self.get_metricdata, disk, disk_usage)
            disk_data = {
                'df_bytes_free': data_func('df_bytes_free'),
                'df_bytes_used_percentage': data_func('df_bytes_used_percentage')
            }
            instance = Df(**disk_data)
            metrics.append(instance)

        return metrics
