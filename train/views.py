from curses.ascii import FS
import datetime
from email import message
from django.http import HttpRequest, HttpResponse ,JsonResponse
from django.shortcuts import render,redirect
from . import models
from django.template.defaulttags import register
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json

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
    train_date = datetime.datetime.strptime(request.POST.get(
        'travel_date')[2:], '%y-%m-%d')
    next_date =datetime.datetime.today() + datetime.timedelta(days=1)
    navbar = {
        'HNav': 'active-nav'
    }
    travel_date_info ={
        'travel_date_no': train_date.strftime("%d") or next_date.strftime("%d"),
        'travel_month_no': train_date.strftime("%m") or next_date.strftime("%m"),
        'travel_year_no': train_date.strftime("%Y") or next_date.strftime("%Y"),
        'travel_month': train_date.strftime('%b') or next_date.strftime('%b'),
        'travel_day': train_date.strftime('%a') or next_date.strftime('%a'),
    }
    
    param = {
        "navbar": navbar,
        'train_to': train_to,
        'train_from': train_from,
        'travel_date_info': travel_date_info
    }
    return render(request, 'train/ResultPage/index.html', param)

    
    
def train_query(request):
    param={}
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



def stationCodeToModel(request):
    allStationCode = models.trainRecord.objects.all().values(
        "Station_Name",
        "Station_Code").distinct()
    return JsonResponse(list(allStationCode),safe = False)

   
