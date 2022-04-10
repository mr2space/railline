from django.db import models

# Create your models here.

 
class trainRoutePath(models.Model):
    train_station_1 = models.CharField(max_length=30, null=False)
    train_station_2 = models.CharField(max_length=30, null=False)
    train_station_3 = models.CharField(max_length=30, null=False)
    train_station_4 = models.CharField(max_length=30, null=False)
    train_station_5 = models.CharField(max_length=30, null=False)

class trainRouteTime(models.Model):
    train_time_starting = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    train_time_1 = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    train_time_2 = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    train_time_3 = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    train_time_4 = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    train_time_5 = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)
    train_time_destination = models.TimeField(
        auto_now=False, auto_now_add=False, null=False)

class trainRecord(models.Model):
    train_no = models.IntegerField(unique=True, null=False)
    train_name = models.CharField(max_length=30, null=False)
    # ----------SEAT INFO ------------------------------->
    train_total_seat = models.IntegerField(null=False,default=0)
    train_general_seat = models.IntegerField(null=False, default=0)
    train_sleeper_seat = models.IntegerField(null=False, default=0)
    train_ac_seat = models.IntegerField(null=False, default=0)
    train_seat_seat = models.IntegerField(null=False, default=0)
    # ----------ROUTE AND TIME INFO -------------------->
    train_starting = models.CharField(max_length=30, null=False)
    train_destination = models.CharField(max_length=30, null=False)
    train_start_date = models.DateField(null=False)
    route_path_id = models.ForeignKey(trainRoutePath, on_delete=models.CASCADE,default = 0)
    route_time_id = models.ForeignKey(
        trainRouteTime, on_delete=models.CASCADE, default=0)

class quotaPrice(models.Model):
    general = models.FloatField()
    sleeper = models.FloatField()
    Ac = models.FloatField()
    Seat = models.FloatField()
