from sys import argv

from project.settings.base import *


if 'test' in argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}  # noqa
