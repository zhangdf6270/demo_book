"""
Django settings for dj_Book project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(1, os.path.join(BASE_DIR, "extra_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'du86odbd4+4guwh+u$6(1atpk74ld4auhtinmb86s046xg-nmt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXT_APPS = [
    'xadmin',
    'crispy_forms',
    'rest_framework',
    'haystack',
    'celery',
    'celery_tasks',
    'captcha',
    'DjangoUeditor',
]

MY_APPS = [
    'apps.user',
    'apps.book',
    'apps.cart',
    'apps.order',
    'apps.message',
    'apps.comment',
    'apps.apis',
    'apps.analyze'
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + MY_APPS



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_Book.urls'

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

WSGI_APPLICATION = 'dj_Book.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'book',
        'HOST': '47.106.185.147',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '952368',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh_Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.INFO

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SEX_CHOICES = [
   ('M', '男人'),
   ('F', '女人'),
]

USER_CHOICES = [
	(0, '普通会员'),
    (1, 'VIP会员'),
	(2, '黄金会员'),
]

DINNER_CHOICES = [
    (0, '待下单'),
	(1, '已下单')
]

PAY_CHOICES = [
    (0, '货到付款'),
    (1, '微信支付'),
    (2, '支付宝支付'),
]

DB_FIELD_VALID_CHOICES = [
    (0, '未删除'),
    (1, '已删除'),
]

############## BEGIN ############
import redis
R = redis.Redis(host='127.0.0.1', port=6379, db=1)
############### END ###########

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':12
}

#########################
## Django Logging  BEGIN
#########################

# LOGGING_DIR 日志文件存放目录
LOGGING_DIR = "./logs"
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s][%(funcName)s][%(lineno)d] > %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s]> %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '%s/django.log' % LOGGING_DIR,
            'formatter': 'standard'
        },  # 用于文件输出
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'mdjango': {
            'handlers': ['console', 'file_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

logger = logging.getLogger("mdjango")

#########################
## Django Logging  END
#########################


# =================全文检索框架配置 start=============
# 搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        #'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 搜索框架
#设置每页显示的数目，默认为20，可以自己修改
HAYSTACK_SEARCH_RESULTS_PER_PAGE  = 8
# =================全文检索框架配置 end=============

# =================邮箱配置 start=============
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = '17683816811@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'qwe123'
# 收件人看到的发件人
EMAIL_FROM = 'zl<1768381681@163.com>'
# =================邮箱配置 end=============


# =================设置redis缓存配置 start=============
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 设置django缓存的数据保存在redis数据库中
        "LOCATION": "redis://127.0.0.1:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# =================设置redis缓存配置 end=============


# =================设置celery配置 start=============
# BROKER_URL = 'redis://127.0.0.1:6379/1'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
# =================设置celery配置 end=============


# =================支付宝配置相关 start=============
APP_ID='2016092200568044'
# 生产支付环境
ALI_PAY_URL=''
# 测试支付环境
ALT_PAY_DEV_URL='https://openapi.alipaydev.com/gateway.do?'

# 网站私钥文件路径
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'key/app_private_key.pem')

# 支付宝公钥文件路径
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'key/alipay_public_key.pem')
# =================支付宝配置相关 end=============


# =================captcha 配置 start=============
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' # 图片中的文字为随机英文字母
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'    # 图片中的文字为数字表达式，如1+2=</span>
# CAPTCHA_TIMEOUT = 2 # 超时(minutes)
CAPTCHA_LENGTH = 4 # 字符个数
CAPTCHA_IMAGE_SIZE = (150, 50)
# =================captcha 配置 end=============