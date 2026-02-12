from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_staff', 'is_active')
    search_fields = ('name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('id',)

