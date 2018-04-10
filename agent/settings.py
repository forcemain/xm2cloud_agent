#! -*- coding: utf-8 -*-


import logging


# Debug Settings
DEBUG = True


# Monitor Settings
MONITOR_SCHEDULER_INTERVAL = 15


# Channel Settings
CHANNEL_SCHEDULER_INTERVAL = 3
CHANNEL_SENDER_DISCONNECT_TIME = 120
CHANNEL_RECEIVER_DISCONNECT_TIME = 120
CHANNEL_SENDER_EVENT_EXPIRED_TIME = 1800
CHANNEL_RECEIVER_EVENT_EXPIRED_TIME = 1800


# Userdata Settings
DEFAULT_USERDATA_PATH = '/etc/xm2cloud_agent/user_data.json'


# Logging Settings
DEFAULT_LOG_LEVEL = logging.WARNING
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'


