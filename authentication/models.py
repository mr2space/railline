from django.db import models
from django.contrib.auth.models import User
import random
import math
import hashlib

from django.db.models.enums import Choices
from django.db.models.expressions import F
# Create your models here
class userCreations(models.Model):
    
    # variable use to store default values in database 
    gender_choices =(
        ('M','Male'),
        ('F','Female')
    )
    
    user_name = models.CharField(max_length=10,default='',unique=True,null=False)
    profile = models.ImageField(
        upload_to='images/', default='—Pngtree—blue default avatar_5938444.png')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=300,null=False)
    email=models.EmailField(null=False,max_length=254,unique=True)
    is_above_18 = models.BooleanField(default=False)
    gender = models.CharField(max_length=1,choices=gender_choices,default='Male')
    address = models.CharField(max_length=100)
    otp = models.CharField(max_length=5,default='00000',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def setPassword(self, raw_password):
        passwd=str(raw_password)
        passwd = hashlib.sha256(passwd.encode())
        return passwd
        
    def otpGenearator(self):
        # variable to store digit use in Otp
        digits = '0123456789'
        otp = ''
        for i in range(5):
            otp += str(math.floor(random.random()*10))
        return otp
    




class userAddon(models.Model):
    user_name = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(
        upload_to='images/', default='—Pngtree—blue default avatar_5938444.png')
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    is_above_18 = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, default='Male')
    phone_no = models.IntegerField(max_length=12,null=False)
    address = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return self.phone_no