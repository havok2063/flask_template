# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2018-08-16 11:43:42
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2018-08-16 16:09:14

from __future__ import print_function, division, absolute_import
import pytest
from flask import url_for
from {{cookiecutter.package_name}}.app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_app(client):
    assert client.get(url_for('index.home')).status_code == 200


def test_ok_status(client):
    res = client.get(url_for('index.status'))
    assert res.json == {'status': 'ok'}

