from base import *
import dj_database_url


DATABASES = { 'default': {} }

DATABASES['default'] = dj_database_url.parse("mysql://bec999e1787895:978e9893@eu-cdbr-west-01.cleardb.com/heroku_9b53a7d93e26e04?reconnect=true")


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
