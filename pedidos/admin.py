from django.contrib import admin
from .models import Pedidos, LineasPedidos
# Register your models here.

class PedidosAdmin(admin.ModelAdmin):
    pass
    #list_display  = ('username')

class LineasAdmin(admin.ModelAdmin):
    pass
    #readonly_fields = ('create_at')
    #list_display = ('producto', 'precio', 'disponible')

admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(LineasPedidos, LineasAdmin)
#admin.site.register([Pedidos, LineasPedidos])