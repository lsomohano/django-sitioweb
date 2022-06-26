from django.shortcuts import render
from servicios.models import Servicios

# Create your views here.

def servicios(request):
    titles = {"title_page":'Servicios',"sub_title_page":'Conoce nuestros servicios.'}
    servicios = Servicios.objects.all()
    return render(request,"servicios/servicios.html",{"titles":titles, "servicios":servicios})