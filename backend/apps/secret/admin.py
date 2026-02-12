from django.contrib import admin
from .models import Secret

@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'title')
    search_fields = ('user_name', 'title')
    list_filter = ('created_at', 'user_name')
    ordering = ('id',)

    def user_name(self, obj):
        return obj.user.name
    user_name.short_description = 'User Name'