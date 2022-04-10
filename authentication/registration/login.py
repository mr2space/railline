from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect


def loginLogic(request):
    navbar = {
        'LNav': 'active-nav',
    }
    param = {
        'navbar': navbar,
    }
    if request.method != 'POST':
        return render(request, 'user/login.html', param)
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    user = authenticate(username=user_name, password=password)
    if user is not(None):
        login(request,user);
        return redirect("/user/profile")
    msg = {
        "heading": "Login Failed",
        "body": "Your Username or Password is incorrect"
    }
    param['msg'] = msg
    return render(request, 'user/login.html', param)
