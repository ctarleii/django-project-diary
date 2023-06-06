from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from school.forms import UserCreationForm
from school.models import News


def index(request):
    content = News.objects.all()
    return render(request, 'news.html', context={
        'content': content
    })


def diary(request):
    return render(request, 'diary.html')


def news(request):
    content = News.objects.all()
    return render(request, 'news.html', context={
        'content': content
    })


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
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


