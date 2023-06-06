from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from school.models import News

# admin.site.register(Permission)
admin.site.register(News)

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
