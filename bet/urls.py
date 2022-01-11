from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:id>', views.update_profile, name = 'update_profile'),
    path('project_post/', views.project_post, name = 'project_post'),
    path('rate_project/', views.rate_project, name = 'rate_project'),
]