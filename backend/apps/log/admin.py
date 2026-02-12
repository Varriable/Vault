from django.contrib import admin
from .models import Log

@admin.register(Log)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__name', 'action', 'timestamp')
    search_fields = ('user__name', 'action')
    list_filter = ('timestamp','user__name', 'action')
    ordering = ('-timestamp',)
