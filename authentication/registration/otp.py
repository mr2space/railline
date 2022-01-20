from django.http import HttpResponse
from django.shortcuts import render, redirect
from .. import models
from django.contrib import messages
from django.contrib.auth.models import User


def otpLogic(request):
    navbar = {
        'HNav': 'bg-success',
        'HWMINav': 'bg-success',
        'LNav': 'bg-success',
        'RNav': 'active-nav',
    }
    if request.method != 'POST':
        return render(request,'user/verification.html',navbar)
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
    return HttpResponse("registered")