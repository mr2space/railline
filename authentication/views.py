from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.template import Context
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def userLogin(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    user = authenticate(username=user_name, password=password)
    if user is None:
        return redirect('/admin/')
    return redirect('/')
