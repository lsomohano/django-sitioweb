from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    titles = {"title_page":'Home',"sub_title_page":'Pagina principal.'}

    return render(request,"ProyectowebApp/home.html",{"titles":titles})


def servicios(request):
    titles = {"title_page":'Servicios',"sub_title_page":'Conoce nuestros servicios.'}

    return render(request,"ProyectowebApp/servicios.html",{"titles":titles})


def tienda(request):
    titles = {"title_page":'Tienda',"sub_title_page":'Los mejores productos para tí.'}

    return render(request,"ProyectowebApp/tienda.html",{"titles":titles})


def blog(request):
    titles = {"title_page":'Blog',"sub_title_page":'Los mejores post de la web.'}

    return render(request,"ProyectowebApp/blog.html",{"titles":titles})


def contacto(request):
    titles = {"title_page":'Contacto',"sub_title_page":'Dejanos tus comentarios.'}

    return render(request,"ProyectowebApp/contacto.html",{"titles":titles})