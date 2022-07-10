from django.urls import path, include

from users.views import Register
from .views import short_view, redirect_url_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('', short_view, name='shorturl'),
]