from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiView.as_view(), name='apiView'),
]