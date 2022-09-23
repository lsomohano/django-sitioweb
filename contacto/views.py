from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

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

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} describe lo siguiente{}".format(nombre,email,contenido),
            "",["lsomohano23@hotmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")
    return render(request,"contacto/contacto.html",{"titles":titles,"formularioContacto":formularioContacto})