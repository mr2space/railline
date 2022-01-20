from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def loginLogic(request):
    navbar = {
        'HNav': 'bg-success',
        'HWMINav': 'bg-success',
        'LNav': 'active-nav',
        'RNav': 'bg-success',
    }
    if request.method != 'POST':
        return render(request, 'user/login.html', navbar)
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    user = authenticate(username=user_name, password=password)
    print("user is ",user)
    if user is None:
        return redirect('/admin/')
    return redirect('/')