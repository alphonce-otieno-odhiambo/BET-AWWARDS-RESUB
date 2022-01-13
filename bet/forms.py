from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=["full_name","country","bio","contact","profile_picture"]
        

class PostForm(forms.ModelForm):
    class Meta:
        model=Post        
        fields=['project_name','category', "description",'project_pic',]

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review        
        fields=['reviews','location']