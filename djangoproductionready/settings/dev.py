from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c+pc(+^19!gm)hmh9zusfe(mtc587)@hc79+s80)_5qz18ch@%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}