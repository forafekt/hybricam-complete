import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe

from serve import app_settings

register = template.Library()


@register.filter(is_safe=True)
def ngjs(obj):
    """ Transform a python object so it can be safely used in javascript/JSON. """
    return mark_safe(json.dumps(obj, cls=DjangoJSONEncoder))


@register.inclusion_tag('manifest/manifest_meta.html', takes_context=True)
def manifest_meta(context):
    """
    Pass all PWA_* settings into the template
    """
    return {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('APP_')
    }


@register.inclusion_tag('manifest/style.html', takes_context=True)
def serve_css(context):
    """
    Pass any style settings into the template
    """
    return {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('CSS_')
    }


@register.inclusion_tag('manifest/js.html', takes_context=True)
def serve_js(context):
    """
    Pass any js settings into the template
    """
    return {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('JAVASCRIPT_')
    }


@register.inclusion_tag('manifest/fonts.html', takes_context=True)
def serve_fonts(context):
    """
    Pass any fonts settings into the template
    """
    return {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('FONT_')
    }
