from django.shortcuts import render

# Create your views here.

def autenticacion(request):
    titles = {"title_page":'Tienda',"sub_title_page":'Los mejores productos para tí.'}
    
    return render(request,"autenticacion/login.html",{"titles":titles})
