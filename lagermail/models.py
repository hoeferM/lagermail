from django.db import models

# Create your models here.

class devicesettings(models.Model):
    device_id = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    reveiver = models.CharField(max_length=200)
    smtp = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
