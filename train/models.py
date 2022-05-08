from django.db import models

# Create your models here.

 
# class trainRoutePath(models.Model):
#     train_station_1 = models.CharField(max_length=30, null=False)
#     train_station_2 = models.CharField(max_length=30, null=False)
#     train_station_3 = models.CharField(max_length=30, null=False)
#     train_station_4 = models.CharField(max_length=30, null=False)
#     train_station_5 = models.CharField(max_length=30, null=False)

# class trainRouteTime(models.Model):
#     train_time_starting = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)
#     train_time_1 = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)
#     train_time_2 = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)
#     train_time_3 = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)
#     train_time_4 = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)
#     train_time_5 = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)
#     train_time_destination = models.TimeField(
#         auto_now=False, auto_now_add=False, null=False)

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
    Seat_1A = models.FloatField(null=False, default=0)
    Seat_2A = models.FloatField(null=False, default=0)
    Seat_3A = models.FloatField(null=False, default=0)
    Seat_SL = models.FloatField(null=False,default=10)
