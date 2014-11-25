#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 25/Nov/2014 11:41

import os
import sys
import json
import logging

from app import handlers
from functools import partial
from tornado import gen, stack_context, options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop, TimeoutError
from tornado.web import Application

options.define('debug', True)
options.define('port', os.environ.get("PORT", 5000))
options.define('domain', 'xxx.heroku.com')
options.define('prefork_process', -1)
options.define('xheaders', False)


@gen.coroutine
def start_server(**settings):
    if not settings:
        settings = options.options.as_dict()
    else:
        settings.update(options.options.as_dict())
    application = Application([(r'/', handlers.MainHandler)], **settings)
    http_server = HTTPServer(application, **{
        'xheaders': options.options.xheaders
    })
    IOLoop.instance()
    with stack_context.NullContext():
        if options.options.prefork_process > -1:
            http_server.bind(options.options.port)
            http_server.start(options.options.prefork_process)
        else:
            http_server.listen(options.options.port)
    logging.info('Running server on https://{domain}:{port}'.format(**settings))
    yield gen.Task(lambda callback: None)


def run(start_callback):
    options.parse_command_line(final=False)
    io_loop = IOLoop.current()
    @gen.coroutine
    def _invoke_callback(wrapped_callback, **stts):
        yield gen.Task(wrapped_callback, **stts)
    shutdown_by_exception = False
    try:
        level = logging.DEBUG if options.options.debug else logging.INFO
        logging.getLogger().setLevel(level)
        io_loop.run_sync(partial(_invoke_callback, start_callback))
    except TimeoutError:
        pass
    except Exception, e:
        shutdown_by_exception = True
        logging.info('Unhandled exception in %s' % sys.argv[0])
        logging.warn(str(e))
    if shutdown_by_exception:
        sys.exit(1)


if __name__ == '__main__':
    try:
        run(start_server)
    except:
        pass
