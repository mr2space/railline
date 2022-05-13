from curses.ascii import FS
from email import message
from django.http import HttpRequest, HttpResponse ,JsonResponse
from django.shortcuts import render,redirect
from . import models
from django.template.defaulttags import register
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# import requests
# from train.trainf.pnr import pnrSearch
# from .forms import *

# def pnr(request):
#     pnr = request.POST.get("pnr-box")
#     print(pnr)
#     # result = pnrSearch(pnr)
#     return HttpRequest("hello")
def index(request,msg={}):
    navbar = {
        'HNav': 'active-nav'
    }
    param = {
        "navbar": navbar
    }
    
    param['msg'] = msg
    return render(request,'index.html',param)


def trainResultPage(request):
    if request.method != 'POST':
        return redirect('/')
    train_to = request.POST.get('train_query_to')
    train_from = request.POST.get('train_query_from')
    navbar = {
        'HNav': 'active-nav'
    }
    param = {
        "navbar": navbar,
        'train_to': train_to,
        'train_from': train_from
    }
    # msg = {
    #     'heading': 'test',
    #     'body': 'body of msg'
    # }
    # param['msg'] = msg
    return render(request, 'train/ResultPage/index.html', param)

    
    
def train_query(request):
    param={}
    if request.method != 'POST':
        return redirect("/")
    arrival = request.POST.get("train_query_from")
    destination = request.POST.get("train_query_to")
    train_des = models.trainRecord.objects.all().filter(
        Station_Code=destination).distinct().values("Train_No")
    train = []
    train_result = {}
    for i in train_des:
        train = train + list(models.trainRecord.objects.all().filter(
            Station_Code=arrival).filter(Train_No=i['Train_No']).values("Train_No"))
    for i in train:
        train_result[i['Train_No']] = list(
            models.trainRecord.objects.all().filter(Train_No=i['Train_No']).values())
        # print(train_result)
        
        
    return JsonResponse(train_result, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def trainQueryByBoardingDestination(request,boarding,destination):
    param = {}
    param['seat_list'] = {'Seat_1A': '1A',
                          'Seat_2A': '2A', 'Seat_3A': '3A', 'Seat_SL': 'SL'}
    train_des = models.trainRecord.objects.all().filter(
        Station_Code=destination).distinct().values("Train_No")
    train = []
    train_result = {}
    for i in train_des:
        train = train + list(models.trainRecord.objects.all().filter(
            Station_Code=boarding).filter(Train_No=i['Train_No']).distinct('Train_No').values("Train_No"))
    for i in train:
        train_result[i['Train_No']] = list(
            models.trainRecord.objects.all().filter(Train_No=i['Train_No']).distinct('Train_No').filter(Station_Code=destination).values())+list(
            models.trainRecord.objects.all().filter(Train_No=i['Train_No']).distinct('Train_No').filter(Station_Code=boarding).values())
        # print(train_result)
    param['train_data'] = train_result
    # return render(request,'train/ResultPage/TrainResultPage.html',param)
    return JsonResponse(train_result,safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def trainQueryTrainInfo(request,train_no):
    train_info = list(models.trainRecord.objects.all().filter(Train_No = train_no).values())
    return JsonResponse(train_info, safe=False)


@register.filter
def getItemsFromDic(my_dic,key):
    return my_dic.get(key)


@api_view(['GET', 'PUT', 'DELETE'])
def trainQuotaPriceList(request):
    priceList = list(models.quotaPrice.objects.all().values())
    return JsonResponse(priceList,safe=False)






# def trainForm(request):
#     param = {}
#     TrainRouteTimeForm = trainRouteTimeForm()
#     if request.method != 'POST':
#         TrainRouteTimeForm = trainRouteTimeForm()
#         TrainRouteform = trainRoutePathForm()
#         TrainRecordForm = trainRecordForm()
#         param['TrainRouteTimeForm'] = TrainRouteTimeForm
#         param['TrainRouteform'] = TrainRouteform
#         param['TrainRecordForm'] = TrainRecordForm
#         return render(request, './train/train.html',param)
#     form = trainRouteTimeForm(request.POST)
#     if form.is_valid():
#         print("IT save")
#         form.save()
#         print("IT save")
#     print("form invalid")
#     return redirect('/train/form')


# def TrainRouteView(request):
#     param = {}
#     if request.method != 'POST':
#         return redirect('/train/form')
#     form = trainRoutePathForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect('/train/form')
    

# def TrainRecordView(request):
#     param = {}
#     if request.method != 'POST':
#         return redirect('/train/form')
#     form = trainRecordForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect('/train/form')
        
