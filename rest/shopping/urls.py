# urls.py

from django.urls import include, path
from rest_framework import routers

from .views import ShoppingItemViewSet

router = routers.DefaultRouter()
router.register('shopping-item', ShoppingItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
