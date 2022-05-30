from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime

class PassangerPersonalData(models.Model):
    def __str__(self):
        return self.personal_full_name
    def setSeatId(self):
        self.seat_id = self.id
        return 0

class PrePassangerData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #personal data ---------------------------------------------
    personal_full_name = models.CharField(max_length=200)
    personal_age = models.IntegerField()
    personal_email = models.EmailField()
    personal_phone_no = models.BigIntegerField()
    
    #SEAT INFO ------------------------------------------------
    seat_id = models.IntegerField(null=True)
    seat_total_count = models.IntegerField()
    seat_type = models.CharField(max_length=30)
    seat_price = models.IntegerField()
    
    train_id = models.IntegerField()
    boarding = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self):
        return self.passenger_personal_detail


class PostPassangerData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #personal data ---------------------------------------------
    personal_full_name = models.CharField(max_length=200)
    personal_age = models.IntegerField()
    personal_email = models.EmailField()
    personal_phone_no = models.BigIntegerField()
    personal_address = models.TextField()
    #SEAT INFO ------------------------------------------------
    payment_id = models.CharField(max_length=200,primary_key=True)
    seat_id = models.CharField(max_length=100)
    seat_total_count = models.IntegerField()
    seat_type = models.CharField(max_length=30)
    seat_price = models.FloatField()
    train_id = models.IntegerField()
    boarding = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    formation_time = models.DateTimeField(
        auto_now=True)
    
    def setSeat(self):
        self.seat_id = self.id
