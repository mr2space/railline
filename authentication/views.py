from django.http import HttpResponse
from authentication.registration.login import loginLogic
from authentication.registration.otp import otpLogic
from authentication.registration.register import registerLogic
from authentication.models import userAddon_saving as userAddons
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from booking.models import PostPassangerData

def userLogin(request):
    return loginLogic(request)

def userRegister(request):
    return registerLogic(request)


def otpVerification(request):
    return otpLogic(request)
    

@login_required(login_url='/user/login')
def profile(request):
    navbar = {
        'LNav': 'active-nav',
    }
    Fullname = request.user.get_full_name()
    try:
        profileAddons = userAddons.objects.get(user_name_id=request.user.id)
        bookingAddons = PostPassangerData.objects.all().filter(user_id=request.user.id).values()
    except:
        profileAddons = {}
    return render(request,"./userProfile/profile.html",{"thisUserAddon":profileAddons,"navbar":navbar,
                                                        "bookingAddons":list(bookingAddons),
                                                        })


@login_required(login_url='/user/login')
def userLogout(request):
    logout(request)
    return redirect("/")