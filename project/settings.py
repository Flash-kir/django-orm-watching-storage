import os

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD')
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get('SECRET_KEY', 'eyJtZXNzYWdlIjoiSGVsbG8hIn0:Xdc-mOFDjs22KsQAqfVfi8PQSPdo3ckWJxPWwQOFhR4')

DEBUG = os.environ.get('DEBUG', False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['127.0.0.1','0.0.0.0'])

if DEBUG:
    ALLOWED_HOSTS = []


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
