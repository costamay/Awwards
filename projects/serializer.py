from rest_framework import serializers
from .models import Profile, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','image', 'description', 'user', 'date_posted', 'link', 'country']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'bio', 'contact']
