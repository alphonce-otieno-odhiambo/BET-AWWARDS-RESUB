from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name','last_name','profile_pic','bio','mobile_number','email']
        

class PostForm(forms.ModelForm):
    class Meta:
        model=Post        
        fields=['issue','project_pic','make','model','year']