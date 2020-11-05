import os

from dotenv import load_dotenv

from project.settings.base import *  # noqa


load_dotenv(dotenv_path=DOTENV_FILE_PATH)  # noqa


# ===========================
# SECURITY
# ===========================

SECRET_KEY = os.getenv('SECRET_KEY')


# ===========================
# DEBUGGING
# ===========================

DEBUG = False


# ===========================
# STATIC FILES (CSS, JavaScript, Images)
# ===========================

STATIC_ROOT = '/var/www/pypublisher/static/'


# ===========================
# HOSTING
# ===========================

ALLOWED_HOSTS = ['*']


# ===========================
# EMAIL
# ===========================

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

ADMINS = [
    ('TamePython', DEFAULT_FROM_EMAIL)
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')

EMAIL_PORT = os.getenv('EMAIL_PORT')

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = True

EMAIL_SUBJECT_PREFIX = '[BUG][TamePython application]'

EMAIL_TIMEOUT = 15


# ===========================
# HTTP
# ===========================

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True


# ===========================
# TEMPLATES
# ===========================

# Set up debugging option to False,
# Django automatically enables the cached template
# loader 'django.template.loaders.cached.Loader'.
# The cached loader then stores the compiled Template in memory.
TEMPLATES[0]['OPTIONS']['debug'] = False  # noqa
