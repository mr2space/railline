# from django.http import HttpRequest
from django.shortcuts import render,redirect
# from train.trainf.pnr import pnrSearch
# from .forms import *

# def pnr(request):
#     pnr = request.POST.get("pnr-box")
#     print(pnr)
#     # result = pnrSearch(pnr)
#     return HttpRequest("hello")
def index(request):
    navbar = {
        'HNav': 'active-nav'
    }
    param = {
        "navbar": navbar
    }
    msg = {
        'heading' : 'test',
        'body':'body of msg'
    }
    param['msg'] = msg
    return render(request,'index.html',param)

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
        
