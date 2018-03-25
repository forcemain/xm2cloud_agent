#! -*- coding: utf-8 -*-


import logging


# debug mode
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'
)


class Logger(object):
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)

        return logger
