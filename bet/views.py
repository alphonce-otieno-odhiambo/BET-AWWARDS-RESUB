from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import ProfileForm, ProjectForm
from . models import *

# Create your views here.
def home(request):
    current_user = request.user
    projo = Project.objects.all()
    return render (request, 'home.html', {"projo":projo})



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
    return render(request, 'profile/create_profile.html', {"form":form})

def project_post(request):
    
    projo= Project.objects.all()
    form = ProjectForm()
    if request.method == "POST":
            form = ProjectForm(request.POST,request.FILES,instance=projo)
            if form.is_valid():
                projo = form.save(commit=False)
                projo.save()
                return redirect('/')
    return render(request, 'project/project.html', {"form":form})

def rate_project(request):
    project = Project.objects.all()
    return render (request, 'project/rate_project.html', {"project":project})





