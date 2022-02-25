from django.contrib.auth import authenticate , login
from django.shortcuts import render, redirect


def loginLogic(request):
    navbar = {
        'LNav': 'active-nav',
    }
    msg={
        "heading":"this is login page",
        "body":"this is body"
    }
    param = {
        'navbar': navbar,
        'msg':msg
    }
    if request.method != 'POST':
        return render(request, 'user/login.html', param)
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    user = authenticate(username=user_name, password=password)
    if user is not(None):
        login(request,user);
        return redirect("/userProfile/profile")
    return redirect('/')