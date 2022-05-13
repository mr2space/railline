from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from train import models as trainModel
from django.contrib.auth.models import User


@login_required(login_url='/user/login')
def userBooking(request,train_no,id):
    # destination_data = trainModel.trainRecord.objects.all().filter(
    #     train_no=train_no).filter(Station_Code = destination).values()
    # boarding_data = trainModel.trainRecord.objects.all().filter(
    #     train_no=train_no).filter(Station_Code=boarding).values()
    # if destination_data <= 0:
    #     return HttpResponse("No seat available")
    return HttpResponse(f"train no : {train_no} \n id: {id}")
    
    
