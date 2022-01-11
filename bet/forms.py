from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name','last_name','profile_pic','bio','email']
        

class PostForm(forms.ModelForm):
    class Meta:
        model=Post        
        fields=['project_name','category','project_pic',]

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review        
        fields=['reviews','location']