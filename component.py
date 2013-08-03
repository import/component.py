# -*- coding: utf-8 -*-
"""
    component
    ~~~~~~~~~

    A module that implements various helper functions to help consume bower
    components from python.

    :copyright: (c) 2013 by Daniel Chatfield
    :license: MIT, see LICENSE for details.
"""

import os
import sys

setup_done = False


def setup(base_dir=None, depth=1, directory='bower_components'):
    """Helper function that fixes python path.

    :param base_dir: Pass __file__ so component knows where your application
                     files are.
    :param depth: The number of times `os.path.dirname()` needs to be
                  called on `base_dir` to get the folder immediately
                  above bower_components Defaults to 1.
    :param directory: The directory defined in .bowerrc (where the
                      components are installed to). Defaults to
                      `bower_components`.
    """
    if setup_done:
        return

    if not base_dir:
        base_dir = __file__

    for i in range(depth):
        base_dir = up_a_level(base_dir)

    bower_path = os.path.join(base_dir, directory)

    sys.path.insert(0, bower_path)

    setup_done = True


def up_a_level(current_pointer):
    """A helper function to traverse up a level of the filesystem"""
    return os.path.dirname(current_pointer)


def require(component_name):
    """A wrapper that allows importing of components as python packages
    """
    setup()
    return __import__(component_name)


def export(object):
    pass
