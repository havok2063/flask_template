# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-08-16 10:36:28
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-08-16 16:09:19

from __future__ import print_function, division, absolute_import
from flask import Blueprint, render_template, jsonify

index = Blueprint("index", __name__)


@index.route('/status/', methods=['GET', 'POST'], endpoint='status')
def status():
    return jsonify({'status': 'ok'})


@index.route('/', methods=['GET'], endpoint='home')
@index.route('/index/', methods=['GET'], endpoint='index')
def home():
    output = {'title': 'home'}
    return render_template('index.html', **output)

