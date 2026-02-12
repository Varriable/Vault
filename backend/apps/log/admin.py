from django.contrib import admin
from .models import Logs

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'action', 'timestamp')
    search_fields = ('user_name', 'action')
    list_filter = ('timestamp','user_name', 'action')
    ordering = ('-timestamp',)

    def user_name(self, obj):
        return obj.user.name
    user_name.short_description = 'User Name'