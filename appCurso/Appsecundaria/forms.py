from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class vender_articulos(forms.Form):
        
    Articulo = forms.CharField(max_length = 40)
    Descripcion = forms.CharField(max_length = 40)
    Precio = forms.IntegerField()


class seleccion_articulos(vender_articulos):
    # Esta clase Agregar hereda todos los campos de la clase vender_articulos
    pass

class AgregarAlCarritoForm(forms.Form):
    Articulo = forms.CharField(max_length=40)
    Descripcion = forms.CharField(max_length=40)
    Precio = forms.IntegerField()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="modificar")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1', 'password2']
        help_text ={k:"" for k in fields}