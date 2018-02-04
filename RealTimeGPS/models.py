# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Datos(models.Model):
#[{"latitude":6.1981541,"longitude":-75.57945219999999,"temp":23.1,"humid":87.2,"timestamp":"2017-05-24T16:20:39.000Z"},
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=30)
