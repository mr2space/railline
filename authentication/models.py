from django.db import models
from django import forms
import random
import hashlib
# Create your models here
class user(models.Model):
    user_name = models.CharField(max_length=10,default='',unique=True)
    profile = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=300)
    email=models.EmailField(null=False,max_length=254,unique=True)
    mobile_no = models.CharField(max_length=50)
    is_above_18 = models.BooleanField(default=False)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
    
    def set_password(self, raw_password):
        passwd=str(raw_password)
        passwd = hashlib.sha256(passwd.encode())
        self.passwd = passwd
        