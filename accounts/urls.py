from django.urls import path
from .views import create_user

urlpatterns = [
    path('signup', create_user, name='signup')
]
