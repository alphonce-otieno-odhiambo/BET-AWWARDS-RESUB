from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name','last_name','profile_pic','bio','mobile_number','email']
        

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("project_name","country", "image", "date_added")