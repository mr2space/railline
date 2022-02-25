from django.http import HttpRequest
from django.shortcuts import render
from train.trainf.pnr import pnrSearch


def pnr(request):
    pnr = request.POST.get("pnr-box")
    print(pnr)
    # result = pnrSearch(pnr)
    return HttpRequest(pnr)
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
    print(param)
    return render(request,'index.html',param)


