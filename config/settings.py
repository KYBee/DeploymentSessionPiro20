from pathlib import Path
# json, ImproperlyConfigured 추가 -> 배포 전 SecretKey 부분을 수정하기 위해서
import os, json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#TODO : 수정이 필요한 부분 -> Key 를 지우고 환경변수나 파일로 접근하도록 수정해야 함
# BASE_DIR은 manage.py가 있는 곳
secret = os.path.join(BASE_DIR, 'secret.json')
with open(secret) as f:
    secrets = json.loads(f.read())

def get_secret(keyword, secrets=secrets):
    try:
        return secrets[keyword]
    except KeyError:
        raise ImproperlyConfigured("No variable : {}".format(keyword))

SECRET_KEY = get_secret("SECRET_KEY")

#TODO : DEBUG 모드가 True라면 Development모드에 적합함. 배포를 위한 버전에서, 그리고 배포를 할 때에는 DEBUG를 False로 바꾸어 배포해야 함
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TODO : ALLOWED_HOSTS 지정이 필요하다면 설정해야 함. 모든 접근을 허용하기 위해서는 '*'을 입력
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#TODO : 만약 DB를 SQLite말고 다른 것을 쓰고 싶다면 수정해야 하는 부분.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#TODO : STATIC_ROOT 를 설정해야 함. NGINX 등의 웹 서버를 사용할 때 웹 서버에서 static 소스를 어디에서 찾아야 하는지를 명시해야함
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home', 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
