import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iy1)%6&-#0(w*b@a$1l47%i++!7vp$=vjv$anp4-d2vyth+h*q'

DATABASES = {
    'default_bak': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'msjung',
        'PASSWORD': 'ahrakfms',
        'HOST': 'myhome',
        'PORT': '3306'
    }
}

INSTALLED_APPS = [
    'db',
    'django_extensions',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True
