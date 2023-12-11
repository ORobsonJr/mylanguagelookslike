from django.shortcuts import render
from .models import User
from django.views.decorators.http import require_GET


# Create your views here.

@require_GET
def find_user_by_username(request):
    try:
        username_ = request.GET.get('username')
        user = User.objects.get(username=username_)
    
        return user

    
    except Exception as e:
        return e
    
    