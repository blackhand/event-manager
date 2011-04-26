
import os

from os.path import dirname, join, realpath

PROJ_DIR = realpath(join(dirname(__file__), '..'))
BASE_DIR = realpath(join(dirname(__file__), '..', '..'))

ADMINS = (
    ('Yonsy Solis', 'yonsy.solis@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'project.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Lima'
LANGUAGE_CODE = 'es-pe'

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(BASE_DIR, 'static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '-0*oge_fiv41d91)qbb#0*#myo@vkwfhy4&it8jyj!bj1j5xs0'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    join(BASE_DIR, "templates"),
)

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # extras
    'south',
    'django_extensions',
    'registration',

    # apps
    'events'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Custom settings

# Google Maps key for default http://127.0.0.1:8000/
GMAPS_API_KEY = 'ABQIAAAAjI5dgVn0vMYU8GWE2dQ1URTpH3CbXHjuCVmaTc5MkkU4wO1RRhT5voP6lpPrYBSsvUxIWKLFPL2SHg'

