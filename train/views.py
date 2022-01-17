from django.https import HttpRequest
from django.shortcuts import render
from train.trainf.pnr import pnrSearch


def pnr(request):
    pnr = request.POST.get("pnr-box")
    print(pnr)
    # result = pnrSearch(pnr)
    return HttpRequest(pnr)
def index(request):
    return render(request,'index.html')


