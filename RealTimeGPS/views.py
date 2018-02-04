# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic  import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from forms import DatosForm 

class index(CreateView):
    template_name = 'index.html' #Plantilla a utilizar
    form_class = AuthenticationForm #Fomulario a utilizar
    success_url = reverse_lazy("RealTimeGPS:mapa") #Redireccionamiento
class sign(CreateView):
    model = User
    template_name = "sign.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('RealTimeGPS:index') 

def mapa(request):
    if request.method == 'POST':
        form = DatosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('RealTimeGPS:index')
    else:
        form = DatosForm()

    return render(request, 'mapa.html', {'form':form})

# def datos(request):
#     if request.method == 'POST':
#         form = DatosForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('RealTimeGPS:index')
#     else:
#         form = DatosForm()

#     return render(request, 'datos.html',  {'form':form})
