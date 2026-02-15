from apps.log.models import Log
from rest_framework import serializers

class LogSerializer(serializers.ModelSerializer):    
    name = serializers.SerializerMethodField()
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Log
        fields = ['id', 'name', 'user_id', 'action', 'timestamp']

    def get_name(self, obj):
        return obj.user.name