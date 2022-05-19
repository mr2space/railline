from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from train import models as trainModel
from django.contrib.auth.models import User


@login_required(login_url='/user/login')
def userBooking(request,train_no,id,destination,boarding):
    
    return HttpResponse(f"train no : {train_no} \n id: {id} \n {destination} \n {boarding}")
    
    
