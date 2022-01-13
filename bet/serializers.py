from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "url","full_name","country","bio","contact","profile_picture","created_on")
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ("id ", "url", "user","project_name","description","project_pic","category","posted_at",)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ("id ", "url","user", 'reviews','post','location',"posted_at",)