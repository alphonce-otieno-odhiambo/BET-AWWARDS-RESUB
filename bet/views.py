from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from django.http.response import JsonResponse
from rest_framework import viewsets, permissions


from .forms import *
from . models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()  
    projo = Post.objects.all()
    return render(request, 'home.html', {"projo":projo, "profile":profile})



def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()           
    return render(request, "profile/profile.html", {"profile": profile, })

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/profile_form.html', {"form":form})

def project_post(request):    
    user = request.user  
    projo = Post.objects.all() 
    form = PostForm()
    if request.method == 'POST':  
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            projo = form.save(commit=False)
            
            projo.save()
            return redirect ('/')        
    else:
        form = PostForm()    
    return render(request,'project/post_project.html',{'form':form})


def review(request,post_id):
  form = ReviewForm()
  post = Post.objects.filter(pk = post_id).first()
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      respo = form.save(commit = False)
      respo.user = request.user
      respo.post = post
      respo.save() 
  return redirect('home')


class PofileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)

    
