from django.shortcuts import render
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path("",views.index,name="site home page"),
    path("train_result",views.trainResultPage),
    path("api/station_code/", views.stationCodeToModel),
    path("api/train_no/<train_no>/", views.trainQueryTrainInfo),
    path("api/train_query/<boarding>/<destination>",views.trainQueryByBoardingDestination),
    path("api/quota_price/",views.trainQuotaPriceList)
    # path("pnr/",views.pnrSearch,name="pnr search"),
    # path("form",views.trainForm,name="Entry For train"),
    # path("trainrouteform", views.TrainRouteView, name="TrainRouteform"),
    # path("trainrecordview", views.TrainRouteView, name="TrainRecordView")
]