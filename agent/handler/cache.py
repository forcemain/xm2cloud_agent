#! -*- coding: utf-8 -*-


import os
import glob
import shutil
import itertools


from agent.util.logger import Logger
from agent.util.enhance import File, Random


logger = Logger.get_logger(__name__)


class CacheHandler(object):
    def __init__(self, cache_path=None):
        self.cache_path = cache_path

    def get_realpath(self, path):
        if path and os.path.exists(path):
            return path
        return self.cache_path

    def exists(self, name, cache_path=None):
        path = self.get_realpath(cache_path)
        file_path = os.path.join(path, name)

        return os.path.exists(file_path), file_path

    def remove(self, name, cache_path=None):
        exists, file_path = self.exists(name, cache_path=cache_path)
        if not exists:
            return
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
            return
        os.remove(file_path)

    def fsize(self, name, cache_path=None):
        exists, file_path = self.exists(name, cache_path=cache_path)
        if not exists or not os.path.isfile(file_path):
            return 0
        return os.path.getsize(file_path)

    def dsize(self, name, cache_path=None):
        exists, file_path = self.exists(name, cache_path=cache_path)
        if not exists:
            return 0
        if os.path.isfile(file_path):
            return self.fsize(name)
        if os.path.isdir(file_path):
            size = 0
            for root, dirs, files in os.walk(file_path):
                size += sum([self.fsize(f) for f in files])

            return size

    def mtime(self, name, cache_path=None):
        exists, file_path = self.exists(name, cache_path=cache_path)
        if not exists:
            return
        return os.path.getmtime(file_path)

    def clear(self, cache_path=None, suffix='json'):
        path = self.get_realpath(cache_path)
        name = os.path.join(path, '*.{0}'.format(suffix))
        glob_files = glob.glob(name)
        for f in glob_files:
            try:
                os.remove(f)
            except OSError as _:
                continue

    def read(self, cache_path=None, batch=50, suffix='json'):
        event_data = []

        path = self.get_realpath(cache_path)
        name = os.path.join(path, '*.{0}'.format(suffix))

        glob_files = glob.glob(name)
        for f in itertools.islice(glob_files, 0, batch):
            f_name = os.path.basename(f)
            try:
                f_content = File.read_content(f)
            except Exception as e:
                logger.warning('Read {0} {1}'.format(f, e))
                continue
            event_data.append((f_name, f_content))

        return event_data

    def write(self, data, cache_path=None, suffix='json'):
        path = self.get_realpath(cache_path)
        name = '{0}.{1}'.format(Random.get_uuid(), suffix)

        file_path = os.path.join(path, name)

        File.write_content(data, file_path)

    def abspath(self, name, cache_path=None):
        _, file_path = self.exists(name, cache_path=cache_path)
        return file_path
