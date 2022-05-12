from statistics import mode
from django.db import models

class PassangerData(models.Model):
    username = models.CharField(max_length=10,unique=True)
    age = models.IntegerField()
    full_name = models.CharField(max_length=200)
    seat_count = models.IntegerField()
    seat_count_by_SL = models.IntegerField()
    seat_count_by_1A = models.IntegerField()
    seat_count_by_2A = models.IntegerField()
    seat_count_by_3A = models.IntegerField()
    seat_price_by_SL = models.IntegerField()
    seat_price_by_1A = models.IntegerField()
    seat_price_by_2A = models.IntegerField()
    seat_price_by_3A = models.IntegerField()
    
