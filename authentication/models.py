from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=300)
    mobileNo = models.CharField(max_length=50)
    email=models.EmailField(default="null",max_length=254)
    age = models.BooleanField(default=False)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    profile = models.ImageField()
