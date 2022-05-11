from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('login', views.userLogin, name="User Login"),
    path('register',views.userRegister,name="user Register"),
    path('verification',views.otpVerification,name="user verification"),
    path('profile', views.profile, name="User Profile"),
    path('logout',views.userLogout,name="logout")
]
