from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializer import userSerializer
from .models import user
# Create your views here.
def accounts(request):
    return render(request,"accounts/accounts.html")

class accountsViews(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
