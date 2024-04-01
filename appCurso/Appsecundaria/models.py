from django.db import models

# Create your models here.
class Vender(models.Model):
    Articulo = models.CharField(max_length = 40)
    Descripcion = models.CharField(max_length = 40)
    Precio = models.IntegerField()
    

class Registrar(models.Model):
    nombre = models.CharField(max_length = 40)
    email = models.CharField(max_length = 40)
    clave = models.IntegerField()

class Agregar(Vender):
    # Esta clase Agregar hereda todos los campos de la clase Vender
    pass

class ProductoEnCarrito(models.Model):
    Articulo = models.CharField(max_length=40)
    Descripcion = models.CharField(max_length=40)
    Precio = models.IntegerField()

