from django.contrib import admin
from .models import CategoriasProductos, Productos
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('producto', 'precio', 'disponible')

admin.site.register(CategoriasProductos, CategoriasAdmin)
admin.site.register(Productos, ProductosAdmin)