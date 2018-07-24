#! -*- coding: utf-8 -*-


import os
import glob
import time
import shutil


from agent.common.logger import Logger
from agent.common.enhance import File, Random


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
        try:
            os.remove(file_path)
        except OSError:
            pass

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
            except OSError:
                pass

    def read(self, cache_path=None, batch=512, suffix='json'):
        event_data = []

        path = self.get_realpath(cache_path)
        name = os.path.join(path, '*.{0}'.format(suffix))

        count = 0
        for f in glob.iglob(name):
            f_name = os.path.basename(f)
            try:
                f_content = File.read_content(f)
            except Exception as e:
                logger.warning('Read {0} {1}'.format(f, e))
                continue
            event_data.append((f_name, f_content))
            count += 1
            if count >= batch:
                break

        return sorted(event_data)

    def write(self, data, cache_path=None, suffix='json'):
        path = self.get_realpath(cache_path)
        uuid, timestamp = Random.get_uuid(), time.time()

        name = '{0}_{1}.{2}'.format(timestamp, uuid, suffix)
        temp = '{0}.{1}'.format(name, 'temp')

        file_path = os.path.join(path, name)
        temp_path = os.path.join(path, temp)

        File.write_content(data, temp_path)
        File.force_move(temp_path, file_path)

    def abspath(self, name, cache_path=None):
        _, file_path = self.exists(name, cache_path=cache_path)
        return file_path
