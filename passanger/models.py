from statistics import mode
from django.db import models


class PassangerPersonalData(models.Model):
    personal_full_name = models.CharField(max_length=200)
    personal_age = models.IntegerField()
    seat_id = models.AutoField(unique=True, null=False)
    seat_category = models.CharField(max_length=20)

class PassangerData(models.Model):
    user_id = models.ForeignKey()
    passenger_personal_detail = models.ForeignKey()
    
    seat_total_count = models.IntegerField()
    
    #SEAT COUNT BY CATEGORY
    seat_count_by_SL = models.IntegerField()
    seat_count_by_1A = models.IntegerField()
    seat_count_by_2A = models.IntegerField()
    seat_count_by_3A = models.IntegerField()
    
    #SINGLE SEAT PRICE
    seat_price_by_SL = models.IntegerField()
    seat_price_by_1A = models.IntegerField()
    seat_price_by_2A = models.IntegerField()
    seat_price_by_3A = models.IntegerField()
    

