# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-08-16 11:14:09
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-08-16 16:05:37

from __future__ import print_function, division, absolute_import
import os

NAME = '{{cookiecutter.package_name}}'.upper()


class Config(object):
    SECRET_KEY = os.environ.get(f'{NAME}_SECRET', os.urandom(24))
    FLASK_SECRET = SECRET_KEY
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    APP_BASE = os.environ.get(f'{NAME}_BASE', '{{cookiecutter.package_name}}')
    projroot = os.path.abspath(os.path.join(APP_DIR, os.pardir, os.pardir))
    PROJECT_ROOT = os.environ.get(f'{NAME}_DIR', projroot)
    os.environ['FLASK_APP'] = os.path.join(APP_DIR, 'app.py')


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'production'
    DEBUG = False
    os.environ['FLASK_ENV'] = ENV


class DevConfig(Config):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
    os.environ['FLASK_ENV'] = ENV


class TestConfig(Config):
    TESTING = True
    DEBUG = True


class CustomConfig(object):
    ''' Project specific configuration.  Always gets appended to an above Config class '''
    pass
