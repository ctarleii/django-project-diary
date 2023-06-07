from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from school.forms import UserCreationForm
from school.models import News, User


def index(request):
    content = News.objects.order_by('-date')[:5]
    return render(request, 'news.html', context={
        'content': content
    })


def news(request):
    content = News.objects.order_by('-date')[:5]
    return render(request, 'news.html', context={
        'content': content
    })


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'article'


def diary(request):
    return render(request, 'diary.html')


def cabinet(request):
    content = User.objects.all()
    context = {
        'content': content
    }
    return render(request, 'cabinet.html', context)


class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


