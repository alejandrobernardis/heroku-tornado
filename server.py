#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 25/Nov/2014 11:41

import time
import logging
from functools import partial
from importlib import import_module
from tornado import gen, options, stack_context
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

try:
    import simplejson as json
except ImportError:
    import json

# imported for option definitions
import options as common_options


SERVER_VERSION = '1.0'
DEFAULT_CONTAINER = 'handlers_list'

_shared_environment = None

__project_name__ = 'B7TSfH'
__project_full_name__ = 'Bit | 7 : Tornado Server for Heroku'
__project_owner__ = ('Asumi Kamikaze, inc',)
__project_author__ = ('Alejandro M. Bernardis',)
__project_version__ = SERVER_VERSION
__project_created__ = (2015, 10)

options.define('server_version', SERVER_VERSION)


class ServerEnvironment(object):
    def __init__(self, application, server, loop):
        self._application = application
        self._server = server
        self._loop = loop

    @property
    def application(self):
        return self._application

    @property
    def server(self):
        return self._server

    @property
    def loop(self):
        return self._loop


def shared_environment():
    global _shared_environment
    if not _shared_environment:
        raise EnvironmentError('The environment has not been defined yet')
    return _shared_environment


class PageNotFoundHandler(RequestHandler):
    def get(self):
        self.set_status(404)
        # TODO(user): Define your custom message here...
        self.finish('ERROR! 404 :P')


@gen.coroutine
def start_server(**settings):
    global _shared_environment
    if not settings:
        settings = options.options.as_dict()
    else:
        settings.update(options.options.as_dict())

    def _parse_handlers_list(module_or_list):
        result = []
        for item in module_or_list:
            if isinstance(item, (tuple, list)) and len(item) in (2, 3, 4):
                result.append(item)
            elif isinstance(item, basestring):
                values = getattr(import_module(item), DEFAULT_CONTAINER, None)
                if not isinstance(values, (tuple, list)):
                    raise RuntimeError(
                        'Module "%s" does not define "%s" attribute like a list'
                        % (item, DEFAULT_CONTAINER))
                result.extend(values)
            else:
                raise RuntimeError('Element not supported: %s' % item)
        return result

    handlers = []
    if settings.get('handlers', False):
        handlers.extend(_parse_handlers_list(settings['handlers']))
    handlers.append((r'/.*', PageNotFoundHandler))
    if 'handlers' in settings:
        del settings['handlers']
    application = Application(handlers, **settings)
    http_server = \
        HTTPServer(application, **{'xheaders': options.options.xheaders})
    io_loop = IOLoop.instance()
    with stack_context.NullContext():
        if options.options.prefork_process > -1:
            http_server.bind(options.options.port)
            http_server.start(options.options.prefork_process)
        else:
            http_server.listen(options.options.port)
    _shared_environment = ServerEnvironment(application, http_server, io_loop)
    logging.debug('--------------')
    logging.debug('** SETTINGS **')
    logging.debug('--------------')
    logging.debug('\n\n%s\n\n' % json.dumps(settings, indent=4, sort_keys=True))
    logging.info('Running server on http://{domain}:{port}'.format(**settings))
    yield gen.Task(lambda callback: None)


@gen.coroutine
def stop_server(**settings):
    environment = shared_environment()
    logging.warn('Shutting down server...')
    environment.server.stop()

    def stop_loop(loop):
        loop.stop()
        logging.info('Au revoir!')

    environment.loop.add_timeout(
        time.time()+5.0, partial(stop_loop, environment.loop))