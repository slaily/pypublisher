import os


# ===========================
# SECURITY
# ===========================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b_3scg0(#a0+edh2*$58908g1o4*g58udc#iy5jczpyvf$7kpm'


# ===========================
# DEBUGGING
# ===========================

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# ===========================
# PATHS
# ===========================

# Directories

# Path to the /pypublisher directory
MAIN_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
# Path to the /pypublisher/project directory
PROJECT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
# Path to the /pypublisher/project/templates directory
TEMPLATES_DIR = os.path.join(PROJECT_DIR, 'templates')
# Path to the /pypublisher/project/static directory
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')

# Files

# Path to the MySQL configuration file
# File contains credentials and other settings related to the database
MYSQL_CONF_PATH = os.path.join(MAIN_DIR, 'mysql.cnf')

# Path to the dotenv file
# File contains sensitive application settings
DOTENV_FILE_PATH = os.path.join(MAIN_DIR, '.env')


# ===========================
# HOSTING
# ===========================

ALLOWED_HOSTS = []


# ===========================
# AUTH
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth
# ===========================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
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
# APPLICATIONS
# ===========================

PREREQUISITES_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'ckeditor',
]

PROJECT_APPS = [
    'project.apps.base.app.BaseConfig',
    'project.apps.blog.app.BlogConfig',
]

INSTALLED_APPS = PREREQUISITES_APPS + PROJECT_APPS

# ===========================
# HTTP
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'project.wsgi.application'


# ===========================
# URLs
# ===========================

ROOT_URLCONF = 'project.urls'


# ===========================
# TEMPLATES
# ===========================

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


# ===========================
# DATABASE
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# ===========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            # Read MySQL credentials from file
            'read_default_file': MYSQL_CONF_PATH,
        },
    }
}


# ===========================
# Django CKEditor
# https://django-ckeditor.readthedocs.io/en/latest/
# ===========================

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 500,
        'toolbar_Custom': [
            [
                'Styles',
                'Format',
                'Bold',
                'Italic',
                'Underline',
                'Strike',
                'Undo',
                'Redo',
                'Link',
                'Unlink',
                'Image',
                'Table',
                'HorizontalRule',
                'TextColor',
                'BGColor',
                'Smiley',
                'SpecialChar',
                'Source',
            ]
        ]
    },
    'special': {
        'toolbar': 'Special',
        'toolbar_Special': [
            {
                'name': 'Edit',
                'items': [
                    'Find',
                    'Replace',
                    '-',
                    'SelectAll'
                ]
            },
            '/',
            {
                'name': 'Insert',
                'items': [
                    'Image',
                    'Link'
                ]
            },
            '/',
            {
                'name': 'Text Format',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                    '-',
                    'RemoveFormat',
                    'CodeSnippet'
                ]
            },
            '/',
            {
                'name': 'Styles',
                'items': [
                    'Styles',
                    'Format',
                    'Font',
                    'FontSize',
                    'TextColor',
                    'BGColor',
                    'NumberedList',
                    'BulletedList',
                    '-', 'Outdent',
                    'Indent',
                    '-',
                    'Blockquote',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                    '-'
                ]
            },
            '/',
            {
                'name': 'Others',
                'items': ['Preview']
            },
        ],
        'extraPlugins': 'codesnippet'
    }
}
