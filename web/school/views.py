from django.shortcuts import render
from django.views.generic import CreateView

from school.models import News


def index(request):
    content = News.objects.all()
    return render(request, 'news.html', context={
        'content': content
    })


def diary(request):
    return render(request, 'diary.html')


def login(request):
    return render(request, 'about.html')


def news(request):
    content = News.objects.all()
    return render(request, 'news.html', context={
        'content': content
    })



