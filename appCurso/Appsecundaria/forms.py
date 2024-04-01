from django import forms 

class vender_articulos(forms.Form):
        
    Articulo = forms.CharField(max_length = 40)
    Descripcion = forms.CharField(max_length = 40)
    Precio = forms.IntegerField()

class registrar_usuario(forms.Form):
        
    nombre = forms.CharField(max_length = 40)
    email = forms.CharField(max_length = 40)
    clave = forms.CharField(max_length = 40)

class seleccion_articulos(vender_articulos):
    # Esta clase Agregar hereda todos los campos de la clase vender_articulos
    pass

class AgregarAlCarritoForm(forms.Form):
    Articulo = forms.CharField(max_length=40)
    Descripcion = forms.CharField(max_length=40)
    Precio = forms.IntegerField()
    
