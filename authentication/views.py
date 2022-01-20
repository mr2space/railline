from authentication.registration.login import loginLogic
from authentication.registration.otp import otpLogic
from authentication.registration.register import registerLogic

def userLogin(request):
    return loginLogic(request)

def userRegister(request):
    return registerLogic(request)


def otpVerification(request):
    return otpLogic(request)
    
