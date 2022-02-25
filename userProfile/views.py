from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout


def profileLogout(request):
    logout(request)
    return redirect("/userProfile/profile")


@login_required(login_url='/user/login')
def profile(request):
    return HttpResponse("hello")