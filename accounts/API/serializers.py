from rest_framework import serializers
from ..models import SSUser


class SSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSUser
        fields = '__all__'


class SSUserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSUser
        fields = ('first_name', 'last_name', 'image', 'email')
