from django.urls import path
from .views import find_user_by_username, auth

urlpatterns = [
    path('get_user', find_user_by_username, name='find_user_by_username'),
    path('auth', auth, name='auth'),
]