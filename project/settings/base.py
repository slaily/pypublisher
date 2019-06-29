import os


# ===========================
# SECURITY
# ===========================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b_3scg0(#a0+edh2*$58908g1o4*g58udc#iy5jczpyvf$7kpm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# ===========================
# PATHS
# ===========================

# Path to the /pypublisher directory
MAIN_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Path to the /pypublisher/project directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path to the /pypublisher/project/templates directory
TEMPLATES_DIR = os.path.join(PROJECT_DIR, 'templates')
# Path to the /pypublisher/project/static directory
STATIC_DIR  = os.path.join(PROJECT_DIR, 'static')


# ===========================
# HOSTING
# ===========================

ALLOWED_HOSTS = []


# ===========================
# PASSWORD VALIDATION
# ===========================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ===========================
# STATIC FILES (CSS, JavaScript, Images)
# ===========================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    STATIC_DIR
]


# ===========================
# INTERNALIZATION
# https://docs.djangoproject.com/en/2.1/topics/i18n/
# ===========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ===========================
# APPLICATION DEFINITION
# ===========================

PREREQUISITES_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'project.apps.base.app.BaseConfig',
    'project.apps.blog.app.BlogConfig',
]

INSTALLED_APPS = PREREQUISITES_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# ===========================
# DATABASE
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# ===========================

DATABASE_NAME = 'your-db-name'
DATABASE_HOST = 'your-db-host'
DATABASE_USER = 'your-db-user'
DATABASE_USER_PASSWORD = 'your-db-user-pass'
DATABASE_CONNECTION_STRING = 'mongodb://{user}:{password}@{host}/{database}'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': DATABASE_NAME,
        'HOST': DATABASE_CONNECTION_STRING.format(
            user=DATABASE_USER,
            password=DATABASE_USER_PASSWORD,
            host=DATABASE_HOST,
            database=DATABASE_NAME
        ),
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_USER_PASSWORD,
    }
}
