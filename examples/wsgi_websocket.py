# entry point for the websocket loop
import os
import gevent.socket
import redis.connection
redis.connection.socket = gevent.socket

import gevent.monkey
gevent.monkey.patch_thread()

os.environ.update(DJANGO_SETTINGS_MODULE='chatserver.settings')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
