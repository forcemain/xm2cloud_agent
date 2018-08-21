#! -*- coding: utf-8 -*-


import time
import psutil
import operator


from functools import partial
from agent.common.enhance import Switch
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class Net(BaseMetric):
    def __init__(self, net_if_in_bytes_persec=None, net_if_out_bytes_persec=None):
        self.net_if_in_bytes_persec = net_if_in_bytes_persec
        self.net_if_out_bytes_persec = net_if_out_bytes_persec

    def get_net_if_in_bytes_persec(self):
        return self.net_if_in_bytes_persec

    def set_net_if_in_bytes_persec(self, net_if_in_bytes_persec):
        self.net_if_in_bytes_persec = net_if_in_bytes_persec

    def get_net_if_out_bytes_persec(self):
        return self.net_if_out_bytes_persec

    def set_net_if_out_bytes_persec(self, net_if_out_bytes_persec):
        self.net_if_out_bytes_persec = net_if_out_bytes_persec

    def to_dict(self):
        data = {}
        if isinstance(self.get_net_if_in_bytes_persec(), MetricData):
            data['net_if_in_bytes_persec'] = self.get_net_if_in_bytes_persec().to_dict()
        if isinstance(self.get_net_if_out_bytes_persec(), MetricData):
            data['net_if_out_bytes_persec'] = self.get_net_if_out_bytes_persec().to_dict()

        return data

    def is_valid(self):
        return True


class Collector(BaseCollector):
    def get_metricdata(self, net_iface, net_count, name):
        tags = {'iface': net_iface}
        for case in Switch(name):
            if case('net_if_in_bytes_persec'):
                name = 'net.if.in.bytes.persec'
                value = net_count[0]

                return MetricData(name, tags, value)
            if case('net_if_out_bytes_persec'):
                name = 'net.if.out.bytes.persec'
                value = net_count[1]

                return MetricData(name, tags, value)
            if case():
                return None

    def get_net_counts(self, name, sample_duration=1):
        net_io_map = {}
        net_io = psutil.net_io_counters(pernic=True)
        for iface, iinfo in net_io.iteritems():
            net_io_map[iface] = {
                'net_if_in_bytes_persec': [iinfo.bytes_recv],
                'net_if_out_bytes_persec': [iinfo.bytes_sent],
            }
        time.sleep(sample_duration)
        net_io = psutil.net_io_counters(pernic=True)
        for iface, iinfo in net_io.iteritems():
            net_io_map[iface]['net_if_in_bytes_persec'].insert(0, iinfo.bytes_recv)
            net_io_map[iface]['net_if_out_bytes_persec'].insert(0, iinfo.bytes_sent)

        return (operator.sub(*net_io_map[name]['net_if_in_bytes_persec']) * 8,
                operator.sub(*net_io_map[name]['net_if_out_bytes_persec']) * 8)

    def start_collects(self):
        metrics = []

        net_if_addrs = psutil.net_if_addrs()
        if not net_if_addrs:
            return metrics

        for net_if in net_if_addrs:
            if net_if.startswith('docker') or net_if.startswith('lo'):
                continue

            net_count = self.get_net_counts(net_if, sample_duration=1)
            data_func = partial(self.get_metricdata, net_if, net_count)

            net_data = {
                'net_if_in_bytes_persec': data_func('net_if_in_bytes_persec'),
                'net_if_out_bytes_persec': data_func('net_if_out_bytes_persec'),
            }
            instance = Net(**net_data)
            metrics.append(instance)

        return metrics


