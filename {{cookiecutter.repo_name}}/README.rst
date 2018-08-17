{{cookiecutter.package_name}}
==============================

{{cookiecutter.short_description}}

| |Build Status|
| |Coverage Status|

------------

This README describes the {{cookiecutter.package_name}} Flask web application. It should include things like a general description, installation instructions, and requirements. It should also include information badges for other services or packages used, e.g., Travis-CI and Coveralls, ReadtheDocs, Astropy, etc.

.. |Build Status| image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}.svg?branch=master
   :target: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}

.. |Coverage Status| image:: https://coveralls.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/badge.svg?branch=master
   :target: https://coveralls.io/github/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}?branch=master


Running the app in Development Mode
-----------------------------------

Using Flask versions 1.0+:
::

    export FLASK_ENV=development
    export FLASK_APP=/path/to/python/{{cookiecutter.package_name}}/app.py
    flask run -p [PORT]

Using Flask versions < 1.0:
::

    run_{{cookiecutter.package_name}} -d -p [PORT]


Running the app for Production
------------------------------

See the `Flask Deployment <http://flask.pocoo.org/docs/1.0/deploying/#deployment>`_ guidelines for hosting
a web app for a production environment.

Nginx + uwsgi
^^^^^^^^^^^^^
This package comes with two preset uwsgi files for self-hosting options with nginx.  A `production.ini` for a host server, or `local.ini` for a local laptop for testing production setups.  If you have uwsgi and nginx already setup, you can run the applicaton with
::

    uwsgi --ini /path/to/python/{{cookiecutter.package_name}}/uwsgi/local.ini --daemonize {{cookiecutter.package_name}}.log




