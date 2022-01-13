from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse
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
    if passwd != confirm_passwd:
        messages.error(request, "Password enter is different ")
        return render(request, 'user/register.html')    
    try:
        print(user_name)
        obj = models.userCreations.objects.get(user_name=user_name);
    except :
        userFunction = register.registerFunctions()
        userFunction.otpGenerator()
        userFunction.userName = user_name
        userFunction.email = Email
        userFunction.sendEmail()
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
        return redirect('/user/verification')
        # messages.success(request,'user created')
    messages.error(request, "Username Already Exist")
    return render(request,'user/register.html')


def otpVerification(request):
    if request.method != 'POST':
        return render(request,'user/verification.html')
    user_name = request.POST.get('user_name')
    user_otp = request.POST.get('user_otp')
    try:
        obj = models.userCreations.objects.get(
            user_name=f"{user_name}",
            otp=user_otp)


    except models.userCreations.DoesNotExist:
        messages.error(request, "Username or OTP not matched")
        return render(request, 'user/verification.html')
    
    if obj == None:
        return redirect('/user/verification')
    user = User.objects.create_user( 
        username = obj.user_name,
        first_name = obj.first_name,
        last_name = obj.last_name,
        password = obj.passwd,
        email = obj.email
    )
    user.save()
    userAddon = models.userAddon_saving(
        user_name=User.objects.get(username=user_name),
        phone_no=obj.phone_no,
        is_above_18=obj.is_above_18,
        gender= obj.gender
    )
    userAddon.save()
    obj.delete()
    return HttpResponse("registered")
    
