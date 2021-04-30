from .base import *

DEBUG = False

ADMINS = (
    ('educa_admin', 'mmccauley4@outlook.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'GiraffeMonkey22',
    }
}