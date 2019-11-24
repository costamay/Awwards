from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =models.ImageField(upload_to= 'profiles/', blank=True, default="profiles/a.jpg")
    bio = models.CharField(max_length=100, default='Welcome to you bio')
    contact = models.CharField(max_length=80)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='')
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=250)
    country = models.CharField(max_length=50)

    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

