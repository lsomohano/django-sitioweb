from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CategoriasProductos(models.Model):
    categoria=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaProducto'
        verbose_name_plural='categoriasProductos'

    def __str__(self):
        return self.categoria

class Productos(models.Model):
    producto=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriasProductos, on_delete=models.CASCADE)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to='tienda',null=True,blank=True)
    disponible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.producto