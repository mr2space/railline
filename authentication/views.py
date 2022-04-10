from authentication.registration.login import loginLogic
from authentication.registration.otp import otpLogic
from authentication.registration.register import registerLogic
from authentication.models import userAddon_saving as userAddons
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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
    print(request.user.id)
    try:
        profileAddons = userAddons.objects.get(user_name_id=request.user.id)
        print(Fullname, profileAddons.profile.url)
    except:
        print("Failed at profileAddon in Auth view")
    return render(request,"./userProfile/profile.html",{"thisUserAddon":profileAddons,"navbar":navbar})