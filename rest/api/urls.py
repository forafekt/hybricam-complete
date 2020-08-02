from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token

from rest.api import views

app_name = 'api'

""" REST URLS """
urlpatterns = [
    path('', views.APIBaseView.as_view(), name='api'),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('allauth/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    re_path('rest-auth/', include('rest.users.urls')),
    re_path('marketing/', include('rest.subscribe.urls'), name='subscribe'),
]

""" APP URLS """
urlpatterns += [

]
