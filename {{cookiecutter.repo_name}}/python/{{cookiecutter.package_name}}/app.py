# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-05-15 10:51:48
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-08-16 16:32:47

from __future__ import print_function, division, absolute_import
import os
from flask import Flask
from {{cookiecutter.package_name}}.controllers.index import index
from {{cookiecutter.package_name}}.settings import ProdConfig, DevConfig, CustomConfig


# set the package name and version
__name__ = '{{cookiecutter.package_name}}'
__version__ = '{{cookiecutter.version}}'


def create_app(debug=None, local=None, object_config=None):
    ''' main web application factory '''

    # set a base name
    base = os.environ.get(f'{__name__.upper()}_BASE', __name__)

    # initiliaze the application
    app = Flask(__name__, static_url_path='/{0}/static'.format(base))
    # set a url prefix
    url_prefix = f'/{__name__}' if local else '/{0}'.format(base)

    # ----------------------------------
    # Load the appropriate Flask configuration object for debug or production
    if not object_config:
        if app.debug or local:
            app.logger.info('Loading Development Config!')
            object_config = type('Config', (DevConfig, CustomConfig), dict())
        else:
            app.logger.info('Loading Production Config!')
            object_config = type('Config', (ProdConfig, CustomConfig), dict())
    app.config.from_object(object_config)

    # ----------------------------------
    # Registration
    register_api(app)
    register_extensions(app, app_base=base)
    register_blueprints(app, url_prefix=url_prefix)

    return app


def register_blueprints(app, url_prefix=None):
    ''' Register the Flask Blueprints used '''

    app.register_blueprint(index, url_prefix=url_prefix)


def register_extensions(app, app_base=None):
    ''' Register the Flask Extensions used '''


def register_api(app, api=None):
    ''' Register the Flask API routes used '''
    pass



