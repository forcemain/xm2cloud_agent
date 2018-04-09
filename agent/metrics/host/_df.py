#! -*- coding: utf-8 -*-


import os
import psutil


from functools import partial
from agent.util.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Df(BaseMetric):
    def __init__(self, df_bytes_total=None, df_bytes_used=None, df_bytes_free=None, df_bytes_used_percentage=None):
        self.df_bytes_total = df_bytes_total
        self.df_bytes_used = df_bytes_used
        self.df_bytes_free = df_bytes_free
        self.df_bytes_used_percentage = df_bytes_used_percentage

    def get_df_bytes_total(self):
        return self.df_bytes_total

    def set_df_bytes_total(self, df_bytes_total):
        self.df_bytes_total = df_bytes_total

    def get_df_bytes_used(self):
        return self.df_bytes_used

    def set_df_bytes_used(self, df_bytes_used):
        self.df_bytes_used = df_bytes_used

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
        if isinstance(self.get_df_bytes_total(), MetricData):
            data['df_bytes_total'] = self.get_df_bytes_total().to_dict()
        if isinstance(self.get_df_bytes_used(), MetricData):
            data['df_bytes_total'] = self.get_df_bytes_used().to_dict()
        if isinstance(self.get_df_bytes_free(), MetricData):
            data['df_bytes_free'] = self.get_df_bytes_free().to_dict()
        if isinstance(self.get_df_bytes_used_percentage(), MetricData):
            data['df_bytes_used_percentage'] = self.get_df_bytes_used_percentage().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, disk, disk_usage, name):
        ddev = os.path.basename(disk.device)
        for case in Switch(name):
            if case('df_bytes_total'):
                name = 'df.bytes.total/device={0},mount={1}'.format(ddev, disk.mountpoint)
                value = disk_usage.total

                return MetricData(name, value)
            if case('df_bytes_used'):
                name = 'df.bytes.used/device={0},mount={1}'.format(ddev, disk.mountpoint)
                value = disk_usage.used

                return MetricData(name, value)
            if case('df_bytes_free'):
                name = 'df.bytes.free/device={0},mount={1}'.format(ddev, disk.mountpoint)
                value = disk_usage.free

                return MetricData(name, value)
            if case('df_bytes_used_percentage'):
                name = 'df.bytes.used.percentage/device={0},mount={1}'.format(ddev, disk.mountpoint)
                value = disk_usage.percent

                return MetricData(name, value)
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
                'df_bytes_total': data_func('df_bytes_total'),
                'df_bytes_used': data_func('df_bytes_used'),
                'df_bytes_free': data_func('df_bytes_free'),
                'df_bytes_used_percentage': data_func('df_bytes_used_percentage')
            }
            instance = Df(**disk_data)
            metrics.append(instance)

        return metrics
