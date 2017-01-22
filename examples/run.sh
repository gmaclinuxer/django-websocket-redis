#!/usr/bin/env bash

uwsgi --ini uwsgi.ini:runserver
uwsgi --ini uwsgi.ini:wsserver
#or
#uwsgi --ini uwsgi_django.ini
#uwsgi --ini uwsgi_ws.ini