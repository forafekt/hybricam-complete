from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ServeConfig(AppConfig):
    name = 'serve'
    verbose_name = _('Serve')
