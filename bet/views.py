from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


from .forms import *
from . models import *

# Create your views here.
def home(request):
    current_user = request.user
    posts = Post.objects.all().order_by('-posted_at')
    return render (request, 'home.html', {"posts":posts})




def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':          
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'profile/update_profile.html', {'form': form})

def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user    
    return render(request,'profile/profile.html',{"current_user":current_user, "user":user, "profiles":profiles})


def project_post(request):    
    user = request.user
    profiles = Profile.objects.filter(user = user).all()
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect ('home')        
        else:
            form = PostForm()    
    return render(request,'project/post_project.html',{'form':form, 'profiles':profiles})





