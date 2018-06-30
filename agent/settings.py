#! -*- coding: utf-8 -*-


import logging


from multiprocessing import cpu_count


# Debug Settings
DEBUG = True


# Event Settings
EVENT_EXPIRED_TIME = 1800


# Engine Settings
ENGINE_SCHEDULER_INTERVAL = 1
ENGINE_MAX_THREADPOOL_SIZE = cpu_count()*8
ENGINE_EVENT_BATCH_SIZE = ENGINE_MAX_THREADPOOL_SIZE


# Monitor Settings
MONITOR_SCHEDULER_INTERVAL = 15


# Heartbeat Settings
HEARTBEAT_SCHEDULER_INTERVAL = 5


# Channel Settings
CHANNEL_SCHEDULER_INTERVAL = 1
CHANNEL_SENDER_DISCONNECT_TIME = 120
CHANNEL_SENDER_EVENT_BATCH_SIZE = 200
CHANNEL_RECEIVER_DISCONNECT_TIME = 120


# Userdata Settings
DEFAULT_USERDATA_PATH = '/etc/xm2cloud_agent/user_data.json'


# Logging Settings
DEFAULT_LOG_LEVEL = logging.DEBUG
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'
