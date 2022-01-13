from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation




CATEGORY_CHOICES = (
	('Designe','Designe'),
	('Informative','Informative'),
	('Functionality','Fun'),	
) 
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    full_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200)
    country = models.CharField(max_length=50)
    profile_picture = CloudinaryField('image')
    contact = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    def _str_(self):
        return f'{self.user.username} profile'
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()
    def _str_(self):
        return self.user.username
        
    

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True,related_name='poste') 
    description = models.TextField(max_length=400)
    project_pic = CloudinaryField('image')
    category = models.CharField(max_length=60,choices=CATEGORY_CHOICES, default="Designe",null=True)
    project_name=  models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.issue 

class Review(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE,null=True)
    reviews = models.TextField(max_length=400)
    location = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.reviews 
    
