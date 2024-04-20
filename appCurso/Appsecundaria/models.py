from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vender(models.Model):
    Articulo = models.CharField(max_length = 40)
    Descripcion = models.CharField(max_length = 40)
    Precio = models.IntegerField()
    

class ProductoEnCarrito(models.Model):
    Articulo = models.CharField(max_length=40)
    Descripcion = models.CharField(max_length=40)
    Precio = models.IntegerField()

#modelo avatar de la ultima clase

class Avatar(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null= True , blank=True)

    #para que se vea la url y el nombre de usuario:
    def __str__(self):

        return f"User:{self.user} - Imagen: {self.imagen}"

#hacer el makemigrations y el migrate
