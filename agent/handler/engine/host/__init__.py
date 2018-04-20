#! -*- coding: utf-8 -*-


from functools import partial
from agent.util.loader import autodiscover_module


autodiscover_module(__name__, __file__)
# provide an automatic refresh interface
"""
example:
    host.autodiscover()
"""
#
autodiscover = partial(autodiscover_module, __name__, __file__)
