from pathlib import Path
import os
import dotenv
from django.core.management.utils import get_random_secret_key
import sys
import dj_database_url

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_6jbso1z+%9-qbavp0656*cxi@)#i$(%=(#2i)ly@osu@zh!w3'

# TODO: generate new secret key
# * python -c 'import secrets; print(secrets.token_hex(24))' 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEVELOPMENT_MODE = os.environ.get("DEVELOPMENT_MODE", True)

# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'base',
    
    'django.contrib.sites',
     
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.microsoft',
    
    'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.trello',
    'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.reddit',
    'allauth.socialaccount.providers.shopify',
    # 'allauth.socialaccount.providers.soundcloud',
    
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    
    "corsheaders",
]

SITE_ID = 2
SOCIALACCOUNT_LOGIN_ON_GET=True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'allauth.account.auth_backends.AuthenticationBackend',
    "corsheaders.middleware.CorsMiddleware",
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT =  BASE_DIR / 'static/media'

STATICFILES_DIRS = [
    BASE_DIR /'static'
]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile', 
            'email',
            'https://www.googleapis.com/auth/gmail.readonly',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
            # 'prompt': 'consent',
        },
        'APP': {
            'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
            'secret': os.environ.get('GOOGLE_SECRET'),
            'key': ''
        },
        'METHOD': 'oauth2',
        'ACCESS_TOKEN_METHOD': 'POST',
        'PROVIDER_ID': 'google',
        # 'ACCESS_TOKEN_URL': 'https://oauth2.googleapis.com/token',
        # 'AUTHORIZATION_URL': 'https://accounts.google.com/o/oauth2/auth',
        'REQUEST_TOKEN_URL': None,
        # 'USER_DATA_URL': 'https://www.googleapis.com/oauth2/v2/userinfo',
        'VERIFIED_EMAIL': True,
        'USE_SSL': True,
        'REDIRECT_URI': 'http://localhost:8000/accounts/google/login/callback/',
        # 'SOCIAL_TOKEN_MODEL': 'allauth.models.SocialToken', # указываем свою модель
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
            'notifications'
        ],
         'APP': {
            'client_id': os.environ.get('GITHUB_CLIENT_ID'),
            'secret': os.environ.get('GITHUB_CLIENT_SECRET'), 
        },
    },
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'


SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_STORE_TOKENS = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)


# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:8080'
# ]\
    
CORS_ALLOW_ALL_ORIGINS = True
    
    
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID'),
# CLIENT_SECRET = os.environ.get('GOOGLE_SECRET')
# REDIRECT_URI = '/'


# # URL для авторизации пользователя
# GOOGLE_AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'

# # URL для обмена авторизационного кода на токены доступа и обновления
# GOOGLE_TOKEN_URL = 'https://oauth2.googleapis.com/token'

# # Параметры авторизации
# params = {
#     'client_id': CLIENT_ID,
#     'redirect_uri': REDIRECT_URI,
#     'response_type': 'code',
#     'scope': 'https://www.googleapis.com/auth/gmail.readonly',
# }

# # URL для получения авторизационного кода
# GOOGLE_AUTH_RIDERECT_URL = GOOGLE_ + '?' + '&'.join([f'{key}={value}' for key, value in params.items()])
