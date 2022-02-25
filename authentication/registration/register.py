from django.shortcuts import render, redirect
from .. import models
from django.contrib import messages
from authentication.registration import addF

def registerLogic(request):
    navbar = {
        'RNav': 'active-nav',
    }
    param = {
        "navbar": navbar
    }
    if request.method != 'POST':
        return render(request,'user/register.html',param)
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
        return render(request, 'user/register.html',param)    
    try:
        print(user_name)
        obj = models.userCreations.objects.get(user_name=user_name);
    except models.userCreations.DoesNotExist:
        userFunction = addF.registerFunctions()
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
    msg = "UserName Already exist"
    param['msg'] = msg
    return render(request,'user/register.html',param)