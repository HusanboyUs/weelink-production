from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.profiles_list),
    path('profile/<int:pk>/', views.profile_detail,),
    
      
]