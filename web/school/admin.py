from django.contrib import admin

from school.models import Person, Permission, News

admin.site.register(Person)
admin.site.register(Permission)
admin.site.register(News)
