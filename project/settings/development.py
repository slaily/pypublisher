from sys import argv

from project.settings.base import *  # noqa


if 'test' in argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}  # noqa

ALLOWED_HOSTS = ['*']
