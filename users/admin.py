from django.contrib import admin

# Register your models here.
from django.contrib.admin import register, ModelAdmin
from .models import CustomUser


@register(CustomUser)
class UserModelAdmin(ModelAdmin):
    pass