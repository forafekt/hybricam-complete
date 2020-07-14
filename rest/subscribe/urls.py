# urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('email-subscribe/', views.EmailSubscribeList.as_view()),
    path('email-subscribe/<int:pk>/', views.EmailSubscribeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
