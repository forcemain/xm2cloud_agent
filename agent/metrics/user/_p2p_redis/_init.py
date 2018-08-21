#! -*- coding: utf-8 -*-


import os
import yaml


from redis import StrictRedis
from functools import partial
from agent.common.enhance import Switch
from agent.metrics.baseloader import BaseLoader
from agent.metrics.basemetric import BaseMetric
from agent.metrics.metric_data import MetricData
from agent.metrics.basecollect import BaseCollector


class P2PRedis(BaseMetric):
    def __init__(self, p2p_redis_dbsize):
        self.p2p_redis_dbsize = p2p_redis_dbsize

    def get_p2p_redis_dbsize(self):
        return self.p2p_redis_dbsize

    def set_p2p_redis_dbsize(self, p2p_redis_dbsize):
        self.p2p_redis_dbsize = p2p_redis_dbsize

    def to_dict(self):
        data = {}
        if isinstance(self.get_p2p_redis_dbsize(), MetricData):
            data['p2p_redis_dbsize'] = self.get_p2p_redis_dbsize().to_dict()

        return data

    def is_valid(self):
        return True


class Loader(BaseLoader):
    def __init__(self, conf=os.path.join(os.path.dirname(__file__), '_init.yaml')):
        with open(conf, 'r+b') as fd:
            self._conf = yaml.load(fd)

    @property
    def init_conf(self):
        return self._conf.get('init_conf', {})

    @property
    def inst_conf(self):
        return self._conf.get('instances', [])

    @property
    def inst_with_tags(self):
        instances_list = []
        for kwargs in self.inst_conf:
            db = kwargs['init'].get('db', 0)
            ins = StrictRedis(**kwargs['init'])
            instances_list.append((db, ins, kwargs['tags']))

        return instances_list


class Collector(BaseCollector):
    enable = False
    loader = Loader() if enable is True else None

    def get_inst_infos(self, db, inst):
        inst_infos = {}
        sections = ['Keyspace']

        for section in sections:
            if section == 'Keyspace':
                db_key = 'db{0}'.format(db)
                inst_infos.update(inst.info(section)[db_key])
            else:
                inst_infos.update(inst.info(section))

        return inst_infos

    def get_tags_infos(self):
        tags_infos_list = []

        for db, inst, tags in self.loader.inst_with_tags:
            inst_infos = self.get_inst_infos(db, inst)
            tags_infos_list.append((inst_infos, tags))

        return tags_infos_list

    def get_metricdata(self, redis_info, tags, name):
        for case in Switch(name):
            if case('p2p_redis_dbsize'):
                name = 'p2p.redis.dbsize'
                value = redis_info.get('keys')

                return MetricData(name, tags, value)
            if case():
                return None

    def start_collects(self):
        metrics = []

        tags_infos = self.get_tags_infos()
        if not tags_infos:
            return metrics

        for redis_info, tags in tags_infos:
            data_func = partial(self.get_metricdata, redis_info, tags)
            redis_data = {
                'p2p_redis_dbsize': data_func('p2p_redis_dbsize')
            }
            instance = P2PRedis(**redis_data)
            metrics.append(instance)

        return metrics
