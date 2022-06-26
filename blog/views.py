from django.shortcuts import render
from blog.models import Posts, Categorias

# Create your views here.

def blog(request):
    titles = {"title_page":'Blog',"sub_title_page":'Los mejores post de la web.'}
    categorias = Categorias.objects.all()
    posts = Posts.objects.all()

    return render(request,"blog/blog.html",{"titles":titles, "posts":posts,"categorias":categorias})