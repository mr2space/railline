from django.shortcuts import render
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path("",views.index,name="site home page"),
    path("pnr/",views.pnrSearch,name="pnr search")
]