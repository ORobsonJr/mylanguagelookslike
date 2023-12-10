from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=200)
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    password = models.CharField(max_length=128)