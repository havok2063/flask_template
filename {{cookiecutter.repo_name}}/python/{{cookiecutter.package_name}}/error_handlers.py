# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-08-16 22:46:56
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-08-16 22:50:48

from __future__ import print_function, division, absolute_import
from flask import request, current_app as app
from flask import Blueprint, render_template


errors = Blueprint('error_handlers', __name__)


def make_error_page(app, name, code, data=None, exception=None):
    ''' creates the error page dictionary for web errors '''
    shortname = name.lower().replace(' ', '_')
    error = {}
    error['title'] = 'Marvin | {0}'.format(name)
    error['page'] = request.url
    error['data'] = data
    error['name'] = name
    error['code'] = code
    error['message'] = exception.description if exception and hasattr(exception, 'description') else None
    app.logger.error('{0} Exception {1}'.format(name, error))
    return render_template('errors/{0}.html'.format(shortname), **error), code


@errors.app_errorhandler(404)
def page_not_found(error):
    ''' custom 404 page not found error '''
    name = 'Page Not Found'
    return make_error_page(app, name, 404, exception=error)
