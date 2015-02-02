#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 29/Jan/2015 18:06

LOCALE = 'en_US'

DOMAIN = 'localhost'
SHORT_DOMAIN = 'short.local'
LOCAL_DOMAIN = 'localhost.local'
API_DOMAIN = 'api.local'

IP = '127.0.0.1'
SHORT_IP = IP
LOCAL_IP = IP
API_IP = IP

PORT = 8000
LOCAL_PORT = PORT
SHORT_PORT = PORT
API_PORT = 9000

LOGIN_URL = '/auth/login'

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_DAY = 60 * 60 * 24
SECONDS_PER_WEEK = SECONDS_PER_DAY * 7
SECONDS_PER_MONTH = SECONDS_PER_WEEK * 4

ASYNC_WORKERS = 8
ASYNC_HTTP_CLIENT = 'tornado.curl_httpclient.CurlAsyncHTTPClient'
PREFORK_PROCESS = -1

SESSION_DAYS = 30
SESSION_SECONDS = SECONDS_PER_DAY * SESSION_DAYS
SESSION_ID = 'sid'
SESSION_COOKIE_ID = 'sid'
SESSION_HEADER_ID = 'X-Session-ID'

DATABASES_KEY = 'db'
KEYVALUES_KEY = 'kv'
OBJECTS_KEY = 'ob'
DEFAULT_KEY = 'default'

ROOT_PATH = './app/data'
CA_PATH = './app/data/etc/CA'
SECRETS_PATH = './app/data/etc/secrets'
LOCALE_PATH = './app/data/var/locale'
FILEOBJECT_PATH = './app/data/var/objects'
PUBLIC_PATH = './app/data/var/public'
STATIC_PATH = './app/data/var/public/static'
TEMPLATE_PATH = './app/data/var/template'
