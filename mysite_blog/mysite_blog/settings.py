import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'blog/templates/blog')
STATIC_DIR = os.path.join(BASE_DIR,'static')




def find_or_create_secret_key():

    SECRET_KEY_DIR = os.path.dirname(__file__)
    SECRET_KEY_FILEPATH = os.path.join(SECRET_KEY_DIR, 'secret_key.py')
    sys.path.insert(1,SECRET_KEY_DIR)

    if os.path.isfile(SECRET_KEY_FILEPATH):
        from secret_key import SECRET_KEY
        return SECRET_KEY
    else:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*(-_=+)'
        new_key = get_random_string(50, chars)
        with open(SECRET_KEY_FILEPATH, 'w') as f:
            f.write("# Django secret key\n# Do NOT check this into version control.\n\nSECRET_KEY = '%s'\n" % new_key)
        from secret_key import SECRET_KEY
        return SECRET_KEY

SECRET_KEY = find_or_create_secret_key()


DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
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

ROOT_URLCONF = 'mysite_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'mysite_blog.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


PASSWORD_HASHERS = [
     'django.contrib.auth.hashers.Argon2PasswordHasher',
     'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
     'django.contrib.auth.hashers.BCryptPasswordHasher',
     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
     'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
 ]

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

LOGIN_REDIRECT_URL = '/'
