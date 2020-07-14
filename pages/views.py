from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home(request):
    return render(request, 'layout/body/home.html', {'home': 'home'})


@require_http_methods(["GET"])
def about(request):
    return render(request, 'layout/body/about.html', {'about': 'about'})


@require_http_methods(["GET"])
def pricing(request):
    return render(request, 'layout/body/pricing.html', {'pricing': 'pricing'})
