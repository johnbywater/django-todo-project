# Overrides
from .settings import *  # noqa: F401

SECRET_KEY = 'lksdf98wrhkjs88dsf8-324ksdm'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gtd',
        'USER': 'you',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
}
