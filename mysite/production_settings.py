from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgre_django',
        'USER': 'db_user',
        'PASSWORD': 'qwer1234',
        'HOST': '$db_host',
        'PORT': '5432',
    }
}
