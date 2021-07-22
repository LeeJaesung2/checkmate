from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_password',
        'user_name',
        'user_gender',
        'user_nation',
        'user_nickname',
        'user_register_time'
    )