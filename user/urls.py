from django.urls import path
from .views import find_user_by_username

urlpatterns = [
    path('get_user', find_user_by_username, name='find_user_by_username')
]