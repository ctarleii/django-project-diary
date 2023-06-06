from django.contrib.auth.models import User
from django.db import models


class Permission(models.Model):
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Право'
        verbose_name_plural = 'Права'


class Person(models.Model):
    first_name = models.CharField(max_length=60, default='')
    last_name = models.CharField(max_length=60, default='')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Permission, on_delete=models.CASCADE)
    telephone_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=90, blank=True)

    def __str__(self):
        return f'{self.username}: {self.role}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class News(models.Model):
    name = models.CharField(max_length=60, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    new = models.CharField(max_length=700)
    date = models.DateTimeField()

    def __str__(self):
        return f'New {self.id}: {self.author}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

