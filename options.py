#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Asumi Kamikaze Inc.
# Licensed under the MIT License.
# Author: Alejandro M. Bernardis
# Email: alejandro (dot) bernardis (at) asumikamikaze (dot) com
# Created: 02/Feb/2015 08:58

from constants import *
from tornado import options

# ips
options.define('ip', IP)
options.define('short_ip', SHORT_IP)
options.define('local_ip', LOCAL_IP)
options.define('api_ip', API_IP)

# domain
options.define('domain', DOMAIN)
options.define('short_domain', SHORT_DOMAIN)
options.define('local_domain', LOCAL_DOMAIN)
options.define('api_domain', API_DOMAIN)

# ports
options.define('port', PORT)
options.define('short_port', SHORT_PORT)
options.define('local_port', LOCAL_PORT)
options.define('api_port', API_PORT)

# settings
options.define('api', False)
options.define('ssl', False)
options.define('debug', True)
options.define('track', False)
options.define('autoreload', False)
options.define('prefork_process', PREFORK_PROCESS)
options.define('locale', LOCALE)
options.define('login_url', LOGIN_URL)
options.define('cookie_secret', None)
options.define('session_cookie', SESSION_COOKIE_ID)
options.define('session_id', SESSION_ID)
options.define('xsrf_cookies', False)
options.define('xsrf_cookie_version', 1)
options.define('xheaders', False)
options.define('compress_response', True)

# paths
options.define('root_path', ROOT_PATH)
options.define('ca_path', CA_PATH)
options.define('static_path', STATIC_PATH)
options.define('template_path', TEMPLATE_PATH)
options.define('locale_path', LOCALE_PATH)
options.define('secrets_path', SECRETS_PATH)
options.define('fileobject_path', FILEOBJECT_PATH)
options.define('public_path', PUBLIC_PATH)

# handlers
# TODO(user): Define your handlers here...
options.define('handlers', [
    'app.handlers'
])