from django.contrib import admin
from .models import Categorias, Posts
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostsAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Posts, PostsAdmin)