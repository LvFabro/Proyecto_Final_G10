from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LvFabro$proyectofinal_db',
        'USER': 'LvFabro',
        'PASSWORD': 'grovestreet',
        'HOST': 'LvFabro.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}




