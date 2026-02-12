from django.contrib import admin
from .models import User, Otp

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_staff', 'is_active')
    search_fields = ('name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('id',)

@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'secret_title', 'code', 'created_at')
    search_fields = ('user_name', 'secret_title', 'code')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def user_name(self, obj):
        return obj.user.name
    user_name.short_description = 'User Name'

    def secret_title(self, obj):
        return obj.secret.title
    secret_title.short_description = 'Secret Title'