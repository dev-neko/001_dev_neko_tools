import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key


# Herokuでエラーを表示させるために追加
DEBUG=False
# DEBUG=True

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS=['*']

# SECRET_KEY=os.environ.get('SECRET_KEY')
SECRET_KEY=get_random_secret_key()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'de_kensaku',
    'support_parts_gen',
]

# Celery設定 REDIS_URL が見つからないローカル環境では第二引数を適用
CELERY_BROKER_URL=os.environ.get('REDIS_URL','redis://localhost')
CELERY_RESULT_BACKEND=os.environ.get('REDIS_URL','redis://localhost')
# これにするとDjangoと同じポスグレに結果が保存される
# CELERY_RESULT_BACKEND = "django-db"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# dj_database_url.config()では、環境変数の一つであるDATABASE_URLを元に接続情報のディクショナリーが入ります。HerokuではディフォルトでDATABASE_URLにPostgresのパスが設定されているため、これ以上の設定は必要ありません。
# https://qiita.com/terappy/items/803ff638d63b3dc09ada
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://devcenter.heroku.com/ja/articles/django-assets
# Herokuの方法→HTML、adminページのcss表示OK
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# この処理を追加することで settings.py の DEBUG が False でも local_settings があればデバッグ環境だと判断されて runserver が可能になる→DEBUGを切り替える必要もなくなる
try:
    from .local_settings import *
except ImportError:
    pass

##################
# Authentication #
##################
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/v1/'
# LOGOUT_REDIRECT_URL = '/accounts/login/'