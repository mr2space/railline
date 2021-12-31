from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.template import Context
from django.core.mail import send_mail
from django.contrib import messages
from . import models
from .registration import register
# Create your views here.


def home(request):
    return redirect('http://mrprince.ml')

def userLogin(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    user = authenticate(username=user_name, password=password)
    if user is None:
        return redirect('/admin/')
    return redirect('/')

def userRegister(request):
    if request.method != 'POST':
        return render(request,'user/register.html')
    user_name = request.POST.get('user_name')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    Email = request.POST.get('email')
    phone_no = request.POST.get('phone_no')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    passwd = request.POST.get("passwd")
    confirm_passwd = request.POST.get("confirm_passwd")
    userFunction = register.registerFunctions()
    userFunction.otpGenerator()
    userFunction.userName = user_name
    userFunction.email = Email
    
    try:
        obj = models.userCreations.objects.get(user_name=user_name);
    except models.userCreations.DoesNotExist:
        userCreation = models.userCreations(
            user_name=user_name,
            passwd=passwd,
            first_name=first_name,
            last_name=last_name,
            email=Email,
            phone_no=phone_no,
            gender=gender,
            is_above_18=age,
            otp=userFunction.code,
        )
        userCreation.save()
        
        return redirect('user/verification')
        # messages.success(request,'user created')
    else:
        messages.error(request, "Error. Message not sent.")
        return render(request,'user/register.html')


def otpVerification(request):
    if request.method != 'POST':
        return render(request,'user/verification.html')
    user_name = request.POST.get('user_name')
    user_otp = request.POST.get('user_otp')
    try:
        obj = models.userCreations.objects.filter(
            entry__username__contains=user_name,
            entry__otp__contains=user_otp,)
    except models.userCreations.DoesNotExist:
        return redirect('/user/verification')
    if not(obj.exists()):
        return redirect('user/verification')
    
