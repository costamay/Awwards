from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer, ProfileSerializer
import datetime as dt
from . forms import ProfileForm, PostForm
def index(request):
    date =dt.date.today()
    posts = Post.objects.all()
    return render(request, 'projects/index.html', {"date":date, "posts":posts })

@login_required(login_url='/accounts/login/?next=/')
def profile(request):
    current_user = request.user
    # if user_id ==None:
    #     user_id=request.user.id
    # current_user = User.objects.get(id = user_id)
    # user=current_user
    # profile = Profile.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    posts = request.user.post_set.all()

    return render(request, 'projects/profile.html', locals())

@login_required(login_url='/accounts/login/?next=/')
def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = current_user
            add.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'projects/profile_update.html',{"form":form })

@login_required(login_url='/accounts/login/?next=/')
def new_post(request):
        current_user = request.user
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('index')
        else:
                form = PostForm()
                return render(request,'projects/new_post.html', {"form":form})

@login_required(login_url='/accounts/login/?next=/')
def vote(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"projects/vote.html", {"post":post})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'projects/search.html',{"message":message})

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Post.objects.all()
        serializers = PostSerializer(all_profile, many=True)
        return Response(serializers.data)