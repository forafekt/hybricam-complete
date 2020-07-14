from rest_framework import status, viewsets

from .models import User
from .serializers import UserSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
