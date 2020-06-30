"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

from .settings.base import env

os.environ.setdefault = env('DJANGO_SETTINGS_MODULE', default="backend.settings.production")
django.setup()
application = get_default_application()
