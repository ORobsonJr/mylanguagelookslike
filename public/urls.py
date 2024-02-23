from django.urls import path
from .views import INDEX

urlpatterns = [
    path('', INDEX.as_view())
]