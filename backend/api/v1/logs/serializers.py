from ....apps.log.models import Log
from rest_framework import serializers

class LogSerializer(serializers.ModelSerializer):    
    name = serializers.SerrializerMethodField()

    class Meta:
        model = Log
        fields = ['id', 'name', 'action', 'created_at']

    def get_user(self,obj):
        return obj.user.name