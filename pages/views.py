from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home(request):
    return render(request, 'layout/body/home.html', {})


@require_http_methods(["GET"])
def about(request):
    return render(request, 'layout/body/about.html', {})
