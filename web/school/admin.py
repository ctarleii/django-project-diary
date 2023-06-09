from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from school.models import News, Student, Lessons, Permissions

# admin.site.register(Permission)
admin.site.register(News)

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    pass
