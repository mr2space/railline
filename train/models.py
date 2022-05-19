from django.db import models
from sqlalchemy import false
class trainRecord(models.Model):
    Train_No = models.IntegerField(null=False)
    # ----------SEAT INFO ------------------------------->
    Seat_1A = models.IntegerField(null=False, default=0)
    Seat_2A = models.IntegerField(null=False, default=0)
    Seat_3A = models.IntegerField(null=False, default=0)
    Seat_SL = models.IntegerField(null=False, default=0)
    
    # ----------ROUTE AND TIME INFO -------------------->
    Station_Name = models.CharField(max_length=30, null=False)
    Station_Code = models.CharField(max_length=30, null=False)
    Route_Number = models.CharField(max_length=30, null=False)
    Arrival_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    Departure_Time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    Distance = models.IntegerField(null=False, default=0)

class quotaPrice(models.Model):
    Seat_1A = models.FloatField(null=False, default=10)
    Seat_2A = models.FloatField(null=False, default=10)
    Seat_3A = models.FloatField(null=False, default=10)
    Seat_SL = models.FloatField(null=False,default=10)

class StationCodeMapper(models.Model):
    Station_Code = models.CharField(max_length=30,null=False,unique=True)
    Station_Name = models.CharField(max_length=50 ,null=False)

    def __str__(self):
        return self.station_name
