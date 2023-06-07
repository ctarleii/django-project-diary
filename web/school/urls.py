from django.urls import path, include

from school import views
from school.views import Register, NewsDetailView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    # path('cabinet/', views.cabinet, name='cabinet'),
    # path('<int:pk>', NewsDetailView.as_view(), name='news-detail')
]

my_patterns = [
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('cabinet/', views.cabinet, name='cabinet'),
]


