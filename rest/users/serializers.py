from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.username
    class Meta:
        model = User
        fields = '__all__'
