# entry point for the Django loop
import os
from django.core.wsgi import get_wsgi_application
os.environ.update(DJANGO_SETTINGS_MODULE='chatserver.settings')
application = get_wsgi_application()
