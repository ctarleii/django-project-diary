from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from school.forms import UserCreationForm, CommentForm
from school.models import News, User, Likes


def index(request):
    # content = News.objects.order_by('-date')[:5]
    content = News.objects.order_by('-date')[:5]
    return render(request, 'index.html', context={
        # 'content': content,
        'content': content
    })


def news(request):
    content = News.objects.order_by('-date')[:15]
    return render(request, 'news.html', context={
        'content': content
    })


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)


class NewsDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан'

    def get_success_url(self, **kwargs):
        return reverse_lazy('news-detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(to=f'/news/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(to=f'/news/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(to=f'/news/{pk}')
        except:
            return redirect(to=f'/news/{pk}')