from statistics import mode
from django.db import models

class PassangerData(models.Model):
    username = models.CharField(max_length=10)
    age = models.IntegerField()
    passanger_full_name = models.CharField(max_length=200)
    seat_count = models.IntegerField()
    seat_count_by_SL = models.IntegerField()
    seat_count_by_1A = models.IntegerField()
    seat_count_by_2A = models.IntegerField()
    seat_count_by_3A = models.IntegerField()
    seat_price_by_SL = models.IntegerField()
    seat_price_by_1A = models.IntegerField()
    seat_price_by_2A = models.IntegerField()
    seat_price_by_3A = models.IntegerField()
    passenger_personal_detail = models.ForeignKey()
        
class PassangerPersonalData(models.Model):
    personal_full_name = models.CharField(max_length=200)
    personal_age = models.IntegerField()
    seat_id = models.AutoField(unique=True,null=False)
    seat_category = models.CharField(max_length=20)
    