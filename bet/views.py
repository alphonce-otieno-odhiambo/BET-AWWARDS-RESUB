from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .forms import *
from . models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.all().order_by('-posted_at')
    
    respos = Review.objects.all().filter().order_by('-posted_at')
    current_user = request.user
    form = ReviewForm()
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
        
    except ObjectDoesNotExist:
        return redirect('update_profile')
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    if request.method == 'POST':  
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')   

    else:
        form = ReviewForm()
    return render(request, 'home.html',{'profiles':profiles,'posts':posts, 'form':form,'respos':respos,'current_user':current_user})





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
  return redirect('index')



