#! -*- coding: utf-8 -*-


import os
import imp
import importlib


def autodiscover_module(package, package_path):
    metrics_modules = []

    cur_dir = os.path.dirname(package_path)
    pyfiles = os.listdir(cur_dir)
    if not pyfiles:
        return

    for fname in pyfiles:
        fpath = os.path.join(cur_dir, fname)

        if os.path.isfile(fpath):
            if fpath.endswith('.py'):
                related_name, _, _ = fname.rpartition('.')
            else:
                continue
        else:
            related_name = fname

        obj = find_related_module(package, related_name)
        if obj is None:
            continue
        metrics_modules.append(obj)

    return metrics_modules


def find_related_module(package, related_name=None):
    try:
        importlib.import_module(package)
    except ImportError:
        package, _, _ = package.rpartition('.')

    try:
        pkg_path = importlib.import_module(package).__path__
    except AttributeError:
        return

    try:
        imp.find_module(related_name, pkg_path)
    except ImportError:
        return

    return importlib.import_module('{0}.{1}'.format(package, related_name))
