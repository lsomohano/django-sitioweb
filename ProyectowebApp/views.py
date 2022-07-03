from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    titles = {"title_page":'Home',"sub_title_page":'Pagina principal.'}

    return render(request,"ProyectowebApp/home.html",{"titles":titles})
