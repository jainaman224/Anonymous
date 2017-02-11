from rest_framework import serializers

from realtime.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone_number')
