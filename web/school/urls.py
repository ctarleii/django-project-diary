from django.urls import path, include

from school import views
from school.views import Register, NewsDetailView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('', views.cabinet, name='cabinet'),
    path('<int:pk>', NewsDetailView.as_view(), name='news-detail')
]