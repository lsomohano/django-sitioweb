from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    titles = {"title_page":'Contacto',"sub_title_page":'Dejanos tus comentarios.'}
    formularioContacto = FormularioContacto()
    if request.method=='POST':
        formularioContacto=FormularioContacto(data=request.POST)

        if formularioContacto.is_valid:
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

    return render(request,"contacto/contacto.html",{"titles":titles,"formularioContacto":formularioContacto})