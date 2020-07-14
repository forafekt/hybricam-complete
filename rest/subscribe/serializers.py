from rest_framework import serializers

from .models import Subscribe


class EmailSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'