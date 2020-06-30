from django.http import HttpResponse
from django.shortcuts import render

from . import app_settings


def serve_funnel(request):
    return render(request, "core/_index.html")  # this is the base template to extend through other html pages.


def service_worker(request):
    response = HttpResponse(
        open(
            app_settings.SERVICE_WORKER_PATH).read(),
        content_type='application/javascript')
    return response


def manifest(request):
    return render(request, 'manifest/manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('APP_')
    })


def offline(request):
    return render(request, "manifest/offline.html")
