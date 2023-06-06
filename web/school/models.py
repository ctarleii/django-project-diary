from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Право'
        verbose_name_plural = 'Права'


class User(AbstractUser):
    pass


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

