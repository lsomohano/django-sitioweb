from django.shortcuts import render
from .models import Productos
# Create your views here.

def tienda(request):
    titles = {"title_page":'Tienda',"sub_title_page":'Los mejores productos para tí.'}
    productos = Productos.objects.all()
    return render(request,"tienda/tienda.html",{"titles":titles, "productos":productos})