from django.shortcuts import render, HttpResponse

from carro.carro import Carro

# Create your views here.

def home(request):
    titles = {"title_page":'Home',"sub_title_page":'Pagina principal.'}
    carro = Carro(request)
    
    return render(request,"ProyectowebApp/home.html",{"titles":titles})
