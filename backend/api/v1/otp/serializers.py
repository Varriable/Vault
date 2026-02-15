from apps.secret.models import Otp
from rest_framework import serializers

class OtpSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    user_id = serializers.IntegerField(write_only=True)
    secret_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Otp
        fields = ['id', 'name', 'user_id', 'secret_id', 'code', 'created_at']
        read_only_fields = ['id', 'name', 'created_at']

    def get_name(self, obj):
        return obj.user.name
