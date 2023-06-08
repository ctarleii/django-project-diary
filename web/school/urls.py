from django.urls import path, include

from school import views
from school.views import Register, NewsDetailView, DelLike, AddLike

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    # path('cabinet/', views.cabinet, name='cabinet'),
    # path('<int:pk>', NewsDetailView.as_view(), name='news-detail')
]

my_patterns = [
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/add_likes/', AddLike.as_view(), name='add_likes'),
    path('news/<int:pk>/del_likes/', DelLike.as_view(), name='del_likes'),
    path('cabinet/', views.cabinet, name='cabinet'),
]


