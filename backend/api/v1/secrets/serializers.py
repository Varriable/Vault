from ....apps.secret.models import Secret
from rest_framework import serializers

class SecretSerializer(serializers.ModelSerializer):    
    name = serializers.SerrializerMethodField()

    class Meta:
        model = Secret
        fields = ['id', 'name', 'title', 'key', 'created_at', 'updated_at']

    def get_name(self,obj):
        return obj.user.name
        
