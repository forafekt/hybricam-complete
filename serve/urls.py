from django.conf.urls import url

from .views import manifest, service_worker, offline, serve_funnel

urlpatterns = [
    url('^$', serve_funnel, name='serve'),
    url('^serviceworker.js$', service_worker, name='serviceworker'),
    url('^manifest.json$', manifest, name='manifest'),
    url('^offline/$', offline, name='offline'),
]
