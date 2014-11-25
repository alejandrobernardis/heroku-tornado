#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 25/Nov/2014 12:13

from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.finish('Heroku+Tornado, running...')