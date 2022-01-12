from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "url","bio","user",  "full_name", "mobile_number", "email")
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ("id ", "url", "user","project_name","description","project_pic","category","posted_at",)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ("id ", "url","user", 'reviews','post','location',"posted_at",)