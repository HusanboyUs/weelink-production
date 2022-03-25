from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    #for loggin and register links
    path('register/', views.registerView, name='registerView'),
    path('login/', views.loginView, name='loginView'),
    #profile
    path('profile/', views.profileView, name='profileView'),
    path('updateProfile/', views.updateProfileView, name='updateProfileView'),
    path('addLink/', views.addProfileLink, name='addProfileLink'),
    path('deleteLink/<str:pk>/', views.deleteProfileLink, name='deleteLink' ),
    #slug for searching the user
    path('<slug:user_slug>', views.userView, name='viewPage'), 
    #path for conatact Page
    path('contact/', views.ContactView, name='contactView'),
    #for password reset function
  

]
 