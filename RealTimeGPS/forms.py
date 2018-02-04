from django import forms
from RealTimeGPS.models import Datos

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        
        fields = [
            'latitude',
            'longitude', 
            'timestamp',
        ]
        labels = {
            'latitude': 'Latitude' ,
            'longitude': 'Longitude',
            'timestamp': 'Timestamp',
        }
        widgets = {
            'latitude': forms.TextInput(attrs={'class':'form-control'}),
            'longitude': forms.TextInput(attrs={'class':'form-control'}),
            'timestamp': forms.TextInput(attrs={'class':'form-control'}),
        }
