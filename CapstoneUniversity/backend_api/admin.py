from django.contrib import admin
from .models import User, Course, UserType


class CustomUserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserType)
admin.site.register(Course)
