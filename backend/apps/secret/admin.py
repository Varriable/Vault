from django.contrib import admin
from .models import Secret, Otp

@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__name', 'title')
    search_fields = ('user__name', 'title')
    list_filter = ('created_at', 'user__name')
    ordering = ('id',)



@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__name', 'secret__title', 'code', 'created_at')
    search_fields = ('user__name', 'secret__title', 'code')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
