#! -*- coding: utf-8 -*-


class GracefulExitException(Exception):
    @staticmethod
    def exitsig_handler(signum, frame):
        raise GracefulExitException()
