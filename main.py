#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 02/Feb/2015 08:26

import sys
import signal
import logging
from functools import partial
from tornado import gen, options, ioloop

# imported for option definitions
import options as common_options


@gen.coroutine
def _initializer(**kwargs):
    logging.info('--------------')
    logging.info('** SERVICES **')
    logging.info('--------------')
    # TODO(user): Initialize your services here...
    logging.info('-')
    logging.info('All services initialized')


def run(start_callback, stop_callback=None, **kwargs):
    options.parse_command_line()
    io_loop = ioloop.IOLoop.current()

    def _on_signal(signum, frame):
        try:
            stop_callback()
        except:
            io_loop.stop()

    signal.signal(signal.SIGHUP, _on_signal)
    signal.signal(signal.SIGINT, _on_signal)
    signal.signal(signal.SIGQUIT, _on_signal)
    signal.signal(signal.SIGTERM, _on_signal)

    @gen.coroutine
    def _invoke_callback(wrapped_callback, **stts):
        yield gen.Task(wrapped_callback, **stts)

    shutdown_by_exception = False
    try:
        level = logging.DEBUG if options.options.debug else logging.INFO
        logging.getLogger().setLevel(level)
        logging.getLogger().handlers[0].setLevel(level)
        io_loop.run_sync(partial(_initializer, **kwargs))
        io_loop.run_sync(partial(_invoke_callback, start_callback))
        if stop_callback is not None:
            func = partial(_invoke_callback, stop_callback)
            io_loop.run_sync(func)
    except ioloop.TimeoutError:
        pass
    except Exception, e:
        shutdown_by_exception = True
        logging.error('Unhandled exception in %s' % sys.argv[0])
        logging.error('Error: %s' % e)
    if shutdown_by_exception:
        sys.exit(1)


if __name__ == '__main__':
    from server import start_server, stop_server
    run(start_server, stop_server)
