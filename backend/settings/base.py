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

# FRONT_ROOT_DIR = os.path.join(ROOT_DIR, 'frontend')

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
    'http://localhost:4200',
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
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'material.admin',
    'material.admin.default',
    # 'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.forms',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
]
THIRD_PARTY_APPS = [
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
]
LOCAL_APPS = [
    'rest.api',
    'rest.shopping.apps.ShoppingConfig',
    'rest.users.apps.UsersConfig',
    'serve.apps.ServeConfig',
    'pages.apps.PagesConfig',
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
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Static files (CSS, JavaScript, Images) & Templates
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static_heroku')
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Tell Django to look in NGLOADER app for Static files and templates.
if DEBUG:
    DJANGO_TEMPLATE_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/templates'),
    )

    STATICFILES_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/static'),
    )
else:  # Change later for production if needed.
    DJANGO_TEMPLATE_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/templates'),
    )

    STATICFILES_DIRS = (
        os.path.join(ROOT_DIR, 'serve/dist/static'),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': DJANGO_TEMPLATE_DIRS,
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
TIME_ZONE = 'UTC'
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

# Serve static files to template.
STYLESHEETS = [
    {
        'src': 'https://unpkg.com/bootstrap-material-design@4.1.1/dist/css/bootstrap-material-design.min.css',
    },
    {
        'src': 'https://unpkg.com/material-components-web@latest/dist/material-components-web.min.css',
    },
    {
        'src': '/static/css/style.css',
    },
    {
        'src': '/static/css/util.css',
    },
]

JAVASCRIPT = [
    {
        'src': 'https://code.jquery.com/jquery-3.2.1.slim.min.js',
    },
    {
        'src': 'https://unpkg.com/popper.js@1.12.6/dist/umd/popper.js',
    },
    {
        'src': 'https://unpkg.com/bootstrap-material-design@4.1.1/dist/js/bootstrap-material-design.js',
    },
    {
        'src': 'https://unpkg.com/material-components-web@latest/dist/material-components-web.min.js',
    },
    {
        'src': 'https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-core@2.0.1/dist/tf-core.min.js',
    },
]
FONTS = [
    {
        'src': 'https://fonts.googleapis.com/icon?family=Material+Icons',
    },
    {
        'src': 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons',
    },
]

# Customize Django admin
MATERIAL_ADMIN_SITE = {
    'HEADER': 'DW STUDIO',  # Admin site header
    'TITLE': 'DASHBOARD',  # Admin site title
    'FAVICON': 'path/to/favicon',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR': 'black',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR': 'black',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE': 'path/to/image',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG': 'path/to/image',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO': 'path/to/image',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG': 'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES': True,  # Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True,  # Show instances counts for each model
    'APP_ICONS': {
        # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name',
        # ...}
        'sites': 'send',
    },
    'MODEL_ICONS': {
        # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
}
