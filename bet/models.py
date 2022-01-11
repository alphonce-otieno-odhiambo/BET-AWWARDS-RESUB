from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = CloudinaryField('image')
    describioption = models.CharField(max_length=250)
    mobile_number = models.IntegerField(blank=True)
    email =  models.CharField(max_length=60) 


    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()
    def _str_(self):
        return self.user.username
        
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    country = models.CharField(max_length=200)
    date_added  = models.DateTimeField(default=timezone.now)
    image =  CloudinaryField('image')

    def save_project(self):
        self.save()

    def upadate_project(self):
        self.save()
    def _str_(self):
        return self.project_name

# class Foo(models.Model):
#     bar = models.CharField(max_length=100)
#     ratings = GenericRelation(Rating, related_query_name='foos')

# Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')
