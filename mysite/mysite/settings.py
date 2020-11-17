import dj_database_url
import os

from decouple import Csv, config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost, 127.0.0.1', cast=Csv())

INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())

SITE_ID = config('SITE_ID', default=1, cast=int)

AUTH_USER_MODEL = 'auth.User'

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

DATA_UPLOAD_MAX_NUMBER_FIELDS = config('DATA_UPLOAD_MAX_NUMBER_FIELDS', default=1000, cast=int)

# Application definition
INSTALLED_APPS = [
    # Django modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Local apps
    'core',

    # External apps
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

# Database
DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL', default='sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))
    )
}

DISABLE_SERVER_SIDE_CURSORS = config('DISABLE_SERVER_SIDE_CURSORS', default=False, cast=bool)

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Password validation
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

# Password reset link expiration days
PASSWORD_RESET_TIMEOUT_DAYS = config('PASSWORD_RESET_TIMEOUT_DAYS', default=1, cast=int)

# Internationalization
LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = config('USE_I18N', default=True, cast=bool)

USE_L10N = config('USE_L10N', default=False, cast=bool)

USE_TZ = config('USE_TZ', default=False, cast=bool)

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = config('STATIC_URL', default='/static/')

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = config('MEDIA_URL', default='/media/')
