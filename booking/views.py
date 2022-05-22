from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from train import models as trainModel
from django.contrib.auth.models import User


@login_required(login_url='/user/login')
def userBooking(request):
    if request.method != 'POST':
        return HttpResponse("Failed")
    param = {}
    param['train_info'] = {
        'train_no': request.POST.get("train-no"),
        'train_id': request.POST.get("train-id"),
        'destination': request.POST.get("destination"),
        'boarding': request.POST.get("boarding"),
        'date': request.POST.get("date"),
        'seat_type': request.POST.get("seat_type"),
        'price': request.POST.get("price"),
    }
    print(param['train_info'])
    #this is just 0.5% of work
    return render(request,'./booking/form.html',param)
    
    
