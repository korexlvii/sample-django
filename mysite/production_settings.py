from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgre_django',
        'USER': 'db_user',
        'PASSWORD': 'qwer1234',
        'HOST': '$DB_HOST',
        'PORT': '5432',
    }
}
