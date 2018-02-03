# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django import forms

class Datos(models.Model):
#[{"latitude":6.1981541,"longitude":-75.57945219999999,"temp":23.1,"humid":87.2,"timestamp":"2017-05-24T16:20:39.000Z"},
    user = models.CharField(max_length=50)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=30)

#This Part might be for forms.py

class DatosForm():
    class Meta:
        model = Datos
        
        fields = [
            'user',
            'latitude',
            'longitude ', 
            'timestamp',
        ]
        labels = {
            'user': 'User' ,
            'latitude': 'Latitude' ,
            'longitude': 'Longitude',
            'timestamp': 'Timestamp',
        }
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'latitude': forms.TextInput(attrs={'class':'form-control'}),
            'longitude ': forms.TextInput(attrs={'class':'form-control'}), 
            'timestamp': forms.TextInput(attrs={'class':'form-control'}),
        }
