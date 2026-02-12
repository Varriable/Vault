from ....apps.user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    exclude = ['password']
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_active', 'is_staff', 'date_joined']


