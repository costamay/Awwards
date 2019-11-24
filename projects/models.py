from django.db import models
from django.contrib.auth.models import User
import datetime as dt

Class Profile(models.Model):
user= models.OneToOneField(User, on_delete=models.CASCADE)
profile_picture =models.ImageField(upload_to= 'profiles/', blank=True, default="profiles/a.jpg")
bio = models.CharField(max_length=100, default='Welcome to you bio')
contact = models.CharField(max_length=80)
