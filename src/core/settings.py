"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@gb1+ahs0@lp30(--&c9+ac@7k0+hi*i&!az-m=j44%h$ohcs2'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.environ.get('DEBUG_MODE') == '1'

ALLOWED_HOSTS = ['django', '127.0.0.1', '0.0.0.0', 'localhost']
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(":")

# Celery Configuration Options`
# CELERY_BROKER_URL = 'amqp://localhost'

# 'amqp://guest:quest@127.0.0.1:5672'
CELERY_BROKER_URL = '{0}://{1}:{2}@{3}:{4}//'.format(
    os.environ.get('MQ_DEFAULT_PROTOCOL', 'amqp'),
    os.environ.get('MQ_DEFAULT_USER', 'guest'),
    os.environ.get('MQ_DEFAULT_PASS', 'guest'),
    os.environ.get('MQ_DEFAULT_HOST', '127.0.0.1'),
    os.environ.get('MQ_DEFAULT_PORT', '5672'),
)

CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# celery -A core beat -l info
CELERY_BEAT_SCHEDULE = {
    'subscribe_notify_beat': {
        'task': 'sport_blog.tasks.subscribe_notify_beat',
        'schedule': crontab(hour='09')
    },
}
# APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'debug_toolbar',
    'sport_blog',
    'account',
]

AUTH_USER_MODEL = 'account.user'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # 'sport_blog.middlewares.SimpleMiddleware',
    # 'sport_blog.middlewares.MetrikaMiddleware',
    # 'sport_blog.middlewares.LoggerMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }


CACHE = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR / "static")
]

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_content', 'static')
# STATIC_ROOT = os.path.join('/tmp', 'static_content', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_content')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    '127.0.0.1',
]

DEFAULT_FROM_EMAIL = "from-admin@sport_blog.com"
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DOMAIN = 'http://127.0.0.1:8000'

# if DEBUG:
#     import socket
#
#     DEBUG_TOOLBAR_PATCH_SETTINGS = True
#
#     INTERNAL_IPS = ['127.0.0.1']
#     ip = socket.gethostbyname(socket.gethostname())
#     ip = '.'.join(ip.split('.')[:-1])
#     ip = f'{ip}.1'
#     INTERNAL_IPS.append(ip)
