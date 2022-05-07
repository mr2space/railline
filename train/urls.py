from django.shortcuts import render
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path("",views.index,name="site home page"),
    path("train_query",views.train_query),
    path("api/<train_no>/", views.train_list)
    # path("pnr/",views.pnrSearch,name="pnr search"),
    # path("form",views.trainForm,name="Entry For train"),
    # path("trainrouteform", views.TrainRouteView, name="TrainRouteform"),
    # path("trainrecordview", views.TrainRouteView, name="TrainRecordView")
]