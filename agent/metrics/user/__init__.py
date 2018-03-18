#! -*- coding: utf-8 -*-


from functools import partial
from agent.util.loader import autodiscover_metric


autodiscover_metric(__name__, __file__)
# provide an automatic refresh interface
"""
example:
    host.autodiscover()
"""
#
autodiscover = partial(autodiscover_metric, __name__, __file__)
