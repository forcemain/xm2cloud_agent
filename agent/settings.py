#! -*- coding: utf-8 -*-


import logging


from multiprocessing import cpu_count


# Debug Settings
DEBUG = True


# Engine Settings
ENGINE_SCHEDULER_INTERVAL = 1
ENGINE_MAX_THREADPOOL_SIZE = cpu_count()*4


# Monitor Settings
MONITOR_SCHEDULER_INTERVAL = 15


# Heartbeat Settings
HEARTBEAT_SCHEDULER_INTERVAL = 5


# Channel Settings
CHANNEL_SCHEDULER_INTERVAL = 1
CHANNEL_SENDER_DISCONNECT_TIME = 120
CHANNEL_SENDER_EVENT_BATCH_SIZE = 240
CHANNEL_RECEIVER_DISCONNECT_TIME = 120
CHANNEL_SENDER_EVENT_EXPIRED_TIME = 1800
CHANNEL_RECEIVER_EVENT_EXPIRED_TIME = 1800


# Userdata Settings
DEFAULT_USERDATA_PATH = '/etc/xm2cloud_agent/user_data.json'


# Logging Settings
DEFAULT_LOG_LEVEL = logging.DEBUG
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'
