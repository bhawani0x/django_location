from rest_framework import serializers
from .models import BaseAddress


class BaseAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAddress
        fields = '__all__'
