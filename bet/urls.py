from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('update-profile',views.update_profile, name='update_profile'),  
    path('profile/<pk>',views.profile, name = 'profile'),
    path('project_post/', views.project_post, name = 'project_post'),
    path('rate_project/', views.rate_project, name = 'rate_project'),
]