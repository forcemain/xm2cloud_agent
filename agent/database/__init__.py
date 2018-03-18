#! -*- coding: utf-8 -*-


import os


def get_basedir():
    return os.path.dirname(os.path.abspath(__file__))


def get_agentdir():
    return os.path.dirname(get_basedir())


def get_projectdir():
    return os.path.dirname(get_agentdir())
