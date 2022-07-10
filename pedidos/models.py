from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Productos
from django.db.models import F, Sum, FloatField
# Create your models here.

User = get_user_model()

class Pedidos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def total(self):
        return self.lineaspedidos_set_aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field=FloatField())
            )["total"]

    class Meta:
        db_table =  "pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['id']

class LineasPedidos(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    productos=models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    pedidos=models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.productos.producto}'

    class Meta:
        db_table = 'lineaspedidos'
        verbose_name = "Linea Pedido"
        verbose_name_plural = "Lineas Pedidos"
        ordering = ['id']