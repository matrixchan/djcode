import os
import sys 

path = '/var/www/djapp'
if path not in sys.path:
    sys.path.insert(0, '/var/www/djapp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djapp.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

