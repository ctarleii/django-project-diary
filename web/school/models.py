from django.contrib.auth.models import AbstractUser
from django.db import models
import statistics


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # is_staff = models.ForeignKey(Permissions, on_delete=models.SET_NULL, null=True)


# class Permission(models.Model):
#     status = models.CharField(max_length=255, default='nothing', null=True)
#     description = models.CharField(max_length=255, default='nothing', null=False)
#     username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


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


class Lessons(models.Model):
    lesson = models.CharField(max_length=255, null=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson} - {self.teacher}'


class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.CharField(max_length=255, null=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

    # lst = []
    # lst.extend(str(n))
    # sum = sum(map(int, lst))
    # res = sum / len(lst)

    # new_rate = sum(map(int, list(str(rate).split(",")[0]))) / len(list(str(self.rate).split(",")[0]))

    def __str__(self):
        return f'{self.username} - {self.lesson}    '


class Meta:
    verbose_name = 'Student'
    verbose_name_plural = 'Students'


class Comments(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Статья', related_name='comments_news',
                                null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=255, verbose_name='Автор комментария',
                               null=True)
    text = models.TextField(verbose_name='Текст комментария', null=True)


class Permissions(models.Model):
    status = models.CharField(max_length=255, default='nothing', null=True)
    description = models.CharField(max_length=255, default='nothing', null=False)
