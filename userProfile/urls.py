from django.urls.conf import include
from django.shortcuts import redirect
from django.urls import path
from . import views



urlpatterns = [
    path('profile', views.profile, name="User Profile"),
    path('logout', views.profileLogout, name="User logout")
]
