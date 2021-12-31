from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path("",views.home,name="prince Home"),
    path('login', views.userLogin, name="User Login"),
    path('register',views.userRegister,name="user Register"),
    path('register',views.user,name="user Register"),
]
