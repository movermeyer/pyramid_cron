pyramid_cron - Simple scheduled tasks for Pyramid
=================================================

.. image:: https://secure.travis-ci.org/storborg/pyramid_cron.png
    :target: http://travis-ci.org/storborg/pyramid_cron
.. image:: https://coveralls.io/repos/storborg/pyramid_cron/badge.png?branch=master
    :target: https://coveralls.io/r/storborg/pyramid_cron
.. image:: https://img.shields.io/pypi/v/pyramid_cron.svg
    :target: https://crate.io/packages/pyramid_cron
.. image:: https://img.shields.io/pypi/dm/pyramid_cron.svg
    :target: https://crate.io/packages/pyramid_cron

Scott Torborg - `Cart Logic <http://www.cartlogic.com>`_

Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

Why it's better than a typical task queue like Celery, Resque, etc:

* No user permissions to worry about: everything is run inside a web request,
  so the task has all the same permissions as your web app.
* Very simple setup, no additional daemons required.
* The API follows Pyramid idioms.

Why it's worse:

* It's not well suited to long-running tasks: everything is run inside a web
  request.
* It does not distribute jobs across workers.
* It does not allow for prioritization of jobs, or have any support for
  non-synchronous tasks.

Documentation is `hosted at Read the Docs <http://pyramid-cron.readthedocs.org/en/latest/>`_.


License
=======

pyramid_cron is licensed under an MIT license. Please see the LICENSE file
for more information.
