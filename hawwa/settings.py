import os
from dotenv import load_dotenv
load_dotenv()
# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['dev.hawwa.online', 'localhost', '127.0.0.1', '0.0.0.0']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://dev.hawwa.online']
CORS_ALLOWED_ORIGINS = ['https://dev.hawwa.online']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSP_DEFAULT_SRC = ("'self'", 'https://dev.hawwa.online')
CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
ROOT_URLCONF = 'hawwa.urls'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'hawwa.CustomUser'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'wellness',
    'adminops',
    'clients',
    'vendors',
    #'django_otp',
    #'django_otp.plugins.otp_totp',
    'hawwa',
    'report_builder',
    'django_tables2',
    'django_filters',
    'django_seed',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hawwastg',
        'USER': 'dbadmin',
        'PASSWORD': '0penP@$$',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

from pathlib import Path
from dotenv import load_dotenv
SECRET_KEY = 'django-insecure-q5%tx0(i2--6%r3=an*il-n_ybv@@#h11&(%y9ls6y5(twhcrr'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Application definition

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

'''
CSP_DEFAULT_SRC = ("'self'", 'https://dev.hawwa.online')
CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
ROOT_URLCONF = 'hawwa.urls'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#Reports
REPORT_BUILDER_INCLUDE = [
    'vendors.models.*',  # Include all models from the vendors app
    'clients.models.*',  # Include all models from the clients app
    'adminops.models.*', # Include all models from the adminops app
]

REPORT_BUILDER_EXCLUDE = [
    'auth.*',  # Exclude auth models
    'admin.*',  # Exclude admin models
]

#WSGI_APPLICATION = 'hawwa.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.infinifyservices.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hello@infinifyservices.com'
EMAIL_HOST_PASSWORD = '0penP@$$'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/django.log',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

