from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField('Название', max_length=255)
    content = models.TextField('Текст')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Название: {self.title} Автор: {self.author_name}'

    class Meta:

        verbose_name = 'New'
        verbose_name_plural = 'News'


class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(News, verbose_name='Публикация', on_delete=models.CASCADE)


class Comments(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Статья', related_name='comments_news', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=255, verbose_name='Автор комментария', null=True)
    text = models.TextField(verbose_name='Текст комментария', null=True)
