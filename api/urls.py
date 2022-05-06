from django.urls import path
from . import views

app_name='api'

urlpatterns = [
    path('', views.apiView.as_view(), name='apiView'),
    path('<slug:slug>', views.UserView.as_view(), name='userView'),
]