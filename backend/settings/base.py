"""
Django settings for backend project.
"""
from daphne import server  # noqa F405
import environ
import os
import re
import sys  # noqa F405

# DIRECTORY ROUTES
# ------------------------------------------------------------------------------
ROOT_DIR = (
        environ.Path(__file__) - 3
)  # (ROOT/backend/settings/base.py - 3 = src/)
env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))

APPS_DIR = ROOT_DIR.path("rest")

# ROUTES
# ------------------------------------------------------------------------------
ASGI_APPLICATION = "backend.routing.application"
WSGI_APPLICATION = "backend.wsgi.application"
CHANNELS_WS_PROTOCOLS = ["graphql-ws"]

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'backend.urls'

# SITE ID
# -----------------------------------------------------------------------------
SITE_ID = 1

# GENERAL & SECURITY
# -----------------------------------------------------------------------------
SECRET_KEY = env("SECRET_KEY", default="SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=0)

CORS_ORIGIN_WHITELIST = (
    'https://localhost:4200',
    'https://192.168.8.101:4200',
    'http://192.168.8.101:4200',
    'http://localhost:8000',
    'http://0.0.0.0:8000',
    'https://hybricam.herokuapp.com',
)

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"

# REST API
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.forms',
    'rest_framework',
    'rest_framework.authtoken',
]
THIRD_PARTY_APPS = [
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'corsheaders',
]
LOCAL_APPS = [
    'rest.api',
    'rest.users.apps.UsersConfig',
    'serve.apps.ServeConfig',
    'rest.subscribe.apps.SubscribeConfig',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# FORMS
# ------------------------------------------------------------------------------
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# Static files (CSS, JavaScript, Images) & Templates
# ------------------------------------------------------------------------------
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static_heroku')
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Tell Django to look in SERVE app for Static files and templates.
# In debug it is possible to have a different static location for local dev if prefered.
if DEBUG:
    DJANGO_TEMPLATE_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/templates'),
    )

    STATICFILES_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/assets'),
    )
else:  # Change later for production if needed. 
    DJANGO_TEMPLATE_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/templates'),
    )

    STATICFILES_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/assets'),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': DJANGO_TEMPLATE_DIRS,
        #'APP_DIRS': True,
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

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# ------------------------------------------------------------------------------
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
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'CET'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# IGNORABLE_404_URLS
# ------------------------------------------------------------------------------
IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = "admin/"
ADMINS = (
    ('Admin', 'admin@admin.com'),
)
MANAGERS = ADMINS

# DJANGO AUTH
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ADAPTER = "rest.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "rest.users.adapters.SocialAccountAdapter"

# REDIS
# ------------------------------------------------------------------------------
REDIS_URL = f'{env("REDIS_URL", default="redis://redis")}/{0}'

# django-channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [REDIS_URL]},
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
USE_DEBUG_TOOLBAR = env.bool("USE_DEBUG_TOOLBAR", default=DEBUG)

if USE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ["debug_toolbar"]
    INTERNAL_IPS = ["127.0.0.1", "0.0.0.0", "localhost", "10.0.2.2", "::1"]
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

    import socket
    import os

    if os.environ.get("USE_DOCKER") == "yes":
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

FONTS = [
    {
        'src': 'https://fonts.googleapis.com/icon?family=Material+Icons',
    },
    {
        'src': 'https://fonts.googleapis.com/css?family=Nunito:300,400,700,800&amp;display=swap',
    }
]

# Serve static files to template.
STYLESHEETS = [
    {
        'src': '/assets/ng_css/styles.css',
    },

]

JAVASCRIPT = [
    {
        'src': '/assets/ng_js/runtime.js',
    },
    {
        'src': '/assets/ng_js/polyfills.js',
    },
    {
        'src': '/assets/ng_js/scripts.js',
    },
    {
        'src': '/assets/ng_js/webphotofilter.js',
    },
    {
        'src': '/assets/ng_js/webphotofilter/webphotofilter.ts3tvfuf.js',
    },
    {
        'src': '/assets/ng_js/webphotofilter/hgl7dero.entry.js',
    },
    {
        'src': '/assets/ng_js/main.js',
    },
]

APP_NAME = 'Hybricam'
APP_DESCRIPTION = "Mobile-browser camera application."
APP_THEME_COLOR = '#fff'
APP_BACKGROUND_COLOR = '#ffffff'
APP_DISPLAY = 'standalone'
APP_SCOPE = '/'
APP_ORIENTATION = 'any'
APP_START_URL = '/'
APP_STATUS_BAR_COLOR = 'default'
APP_DIR = 'ltr'
APP_LANG = 'en-US'
