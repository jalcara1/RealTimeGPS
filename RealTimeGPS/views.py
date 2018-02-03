# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from models import DatosForm 

def index(request):
    return render(request, 'index.html', {})

def sign(request):
    return render(request, 'sign.html', {})

def datos(request):
    if request.method == 'POST':
        form = DatosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('RealTimeGPS:index')
    else:
        form = DatosForm()

    return render(request, 'nuevo.html',  {'form':form})
            
