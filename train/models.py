from django.db import models

# Create your models here.


class trainRecord(models.Model):
    trainId =models.AutoField(_(""))
    trainName = models.models.CharField(max_length=50)
    