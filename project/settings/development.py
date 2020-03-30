import os

from sys import argv

from dotenv import load_dotenv

from project.settings.base import *  # noqa


load_dotenv(dotenv_path=DOTENV_FILE_PATH)  # noqa

if 'test' in argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}  # noqa


# ===========================
# SECURITY
# ===========================

SECRET_KEY = os.getenv('SECRET_KEY')


# ===========================
# HOSTING
# ===========================

ALLOWED_HOSTS = ['*']


# ===========================
# EMAIL
# ===========================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')

EMAIL_PORT = os.getenv('EMAIL_PORT')
