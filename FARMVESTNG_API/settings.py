from dj_database_url import parse as db_url
import os
from unipath import Path
from decouple import config

BASE_DIR = Path(__file__).parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "m0!$_wv_z5p$^90ua=mchpllq#-^%tl5_upf#%#u=hd=c+@t56"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "django_celery_beat",
    "phonenumber_field",
    "django_countries",
    "drf_yasg",
    # local apps
    "User",
    "farms",
    "Investment",
    "Referral",
    "transaction",
    "wallet",
]

AUTH_USER_MODEL = "User.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "FARMVESTNG_API.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "FARMVESTNG_API.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    "default": config(
        "DATABASE_URL", default="sqlite:///" + BASE_DIR.child("db.sqlite3"), cast=db_url
    )
}

DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql_psycopg2"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# REDIS CONFIGURATIONS FOR CELERY
BROKER_URL = config("REDIS_URL")
BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_ROOT = "uploaded"
MEDIA_URL = "/media/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880

# EMAIL SETTINGS

"""
Default mailing service is disabled in favor of sendgrid
"""

"""
EMAIL_USE_TLS = eval(os.getenv('EMAIL_USE_TLS', 'False'))
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '567'))
"""

# CORS CONFIG
CORS_ORIGIN_WHITELIST = config("CORS_ORIGIN_WHITELIST").split(",")

# REST FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}

# Ucomment the next line if you have custom User model
# AUTH_USER_MODEL = 'app.Model'

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

USE_HEROKU = config("USE_HEROKU", default=False, cast=bool)
if USE_HEROKU:
    import django_heroku

    django_heroku.settings(locals())

# Store files to s3
USE_S3_STORAGE = config("USE_S3_STORAGE", default=False, cast=bool)

if USE_S3_STORAGE:
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    # STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_LOCATION = "static"
    S3_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATIC_URL = S3_URL

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
