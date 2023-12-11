from django.shortcuts import render
from .models import User
from django.views.decorators.http import require_GET


# Create your views here.

@require_GET
def find_user_by_username(request):
    username_ = request.GET.get('username')

    try:
        user_ = User.objects.get(username=username_)
        return render(request, 'user.html', {'username:': user_})         

    
    except User.DoesNotExist:
        return render(request, 'index.html', {'username:': None}, status=404)         

    
    
    