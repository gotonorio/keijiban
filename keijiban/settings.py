"""
Django settings for keijiban project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "register.apps.RegisterConfig",
    "bbs.apps.BbsConfig",
    "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "keijiban.middleware.UAmiddleware",
]

ROOT_URLCONF = "keijiban.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "keijiban.context_processors.version_no",
            ],
        },
    },
]

WSGI_APPLICATION = "keijiban.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "kb.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------------------------
# user setting
# ------------------------------------------------------------------
VERSION_NO = "1.0.0 2024-06-05"
AUTH_USER_MODEL = "register.User"
# 写真サイズは5MB以下
LIMMIT_IMAGE_SIZE = 5242880
CSRF_TRUSTED_ORIGINS = ["https://*.sophiagardens.org"]

# ファイルアップロード用
# https://qiita.com/okoppe8/items/86776b8df566a4513e96
# アップロードファイルなどを読み込む際のフォルダの場所を記述
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# サービス内でmediaフォルダのURLパスを設定
MEDIA_URL = "/media/"
# 掲示板用にディレクトリを設定する。
IMAGE_PATH = "keijiban"

LOGIN_URL = "register:login"
LOGIN_REDIRECT_URL = "bbs:file_list"
# ログアウトメッセージ表示のため、コメントアウトする。
# LOGOUT_REDIRECT_URL = "bbs:list"
# ブラウザを閉じたらログアウトさせる。
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",
    "markdown.extensions.codehilite",
]

# settings.pyの切り替え
try:
    from .private_settings import *
except ImportError:
    pass

try:
    from .local_settings import *
except ImportError:
    pass

# For debugging
if DEBUG:
    # 開発環境における静的ファイルの場所を指定する。
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    # will output to your console
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )
else:
    # for nginx
    STATIC_ROOT = "/code/static"
    # will output to logging file
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        filename="/my_log_file.log",
        filemode="a",
    )
