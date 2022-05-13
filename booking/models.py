from django.db import models
from django.contrib.auth.models import User
from django.db import models


class PassangerPersonalData(models.Model):
    personal_full_name = models.CharField(max_length=200)
    personal_age = models.IntegerField()
    seat_id = models.IntegerField()
    # seat_id = models.AutoField(unique=True, null=False)
    seat_category = models.CharField(max_length=20)

    def __str__(self):
        return self.personal_full_name
    def setSeatId(self):
        self.seat_id = self.id
        return 0

class PassangerData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger_personal_detail = models.ForeignKey(
        PassangerPersonalData, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.passenger_personal_detail
