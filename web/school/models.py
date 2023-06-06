from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    class Meta:

        verbose_name = 'New'
        verbose_name_plural = 'News'
