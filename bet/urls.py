from django.urls import path , include
from . import views

from . import views as main_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('department', views.PofileView),
router.register('employee', views.PostView),
router.register('employee', views.ReviewView),

urlpatterns = [
    path('', views.home , name = 'home'),
    path('update-profile',views.update_profile, name='update_profile'),  
    path('profile/<pk>',views.profile, name = 'profile'),    
    path('project_post/',views.project_post, name = 'project_post'),
    path('review/<post_id>', views.review,name='review'),
    path('apis', include(router.urls)),
]