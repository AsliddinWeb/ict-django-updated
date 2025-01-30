from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ict-for-students.uz', 'www.ict-for-students.uz', '167.71.49.146', 'localhost']


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'ict_db',
         'USER': 'ict_user',
         'PASSWORD': 'Bo^725726lyKGerYJ',
         'HOST': 'localhost',
         'PORT': '',
     }
}