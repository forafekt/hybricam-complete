from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class SubscribeConfig(AppConfig):
    name = 'rest.subscribe'
    verbose_name = _('Email Subscriptions')
