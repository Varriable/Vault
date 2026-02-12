from ....apps.secret.models import Otp
from rest_framework import serializers

class OtpSerializer(serializers.ModelSerializer):    
    name = serializers.SerrializerMethodField()

    class Meta:
        model = Otp
        fields = ['id', 'name', 'code', 'created_at']

    def get_name(self,obj):
        return obj.user.name
