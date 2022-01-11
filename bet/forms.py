from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio","email")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("project_name","country", "image", "date_added")