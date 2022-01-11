from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import ProfileForm, ProjectForm
from . models import *

# Create your views here.
def home(request):
    current_user = request.user
    projo = Project.objects.all()
    return render (request, 'home.html', {"projo":projo})




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





