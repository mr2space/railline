from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def accounts(request):
    return render(request,"accounts/accounts.html")
