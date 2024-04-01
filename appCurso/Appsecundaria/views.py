from django.http import request , HttpResponse
from django.shortcuts import render , redirect
from Appsecundaria.models import Vender , Registrar , Agregar , ProductoEnCarrito 
from Appsecundaria.forms import vender_articulos , registrar_usuario , seleccion_articulos , AgregarAlCarritoForm
from django.template import loader


def home(request):

    with open("C:/Users/jotae/OneDrive/Escritorio/appPractica/appCurso/Appsecundaria/templates/home.html") as file:
        indice_html = file.read()
    #pasar el nombre de la plantilla, no el contenido
    return render(request, 'home.html')

def casa(request):
     
    productos = Vender.objects.all()
    dicc = {"productos": productos}
    plantilla = loader.get_template("home.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def Venta(request):

    with open("C:/Users/jotae/OneDrive/Escritorio/appPractica/appCurso/Appsecundaria/templates/formulario_articulos.html") as file:
        formulario_html = file.read()
    return render(request, "formulario_articulos.html")

def Lista(request):

    productos = Vender.objects.all()
    dicc = {"productos": productos}
    plantilla = loader.get_template("lista.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alta_articulo(request):

    if request.method == "POST":
      #llamar a mi formulario creado en forms.py:
        formulario = vender_articulos(request.POST)
        if formulario.is_valid():
           articulo_nuevo = Vender( Articulo = request.POST["Articulo"],Descripcion = request.POST["Descripcion"], Precio = request.POST["Precio"])
           articulo_nuevo.save()
        return render(request , "creado.html")
        
    
def carga(request):
   return render(request , "login.html")

def carrito(request):
   return render(request , "carrito.html")

def alta_usuario(request):

        if request.method == "POST":
          formularioderegistro = registrar_usuario(request.POST)
        if formularioderegistro.is_valid():
           articulo_nuevo = Registrar( nombre = request.POST["nombre"], email = request.POST["email"], clave = request.POST["clave"])
           articulo_nuevo.save()
        return render(request , "usuariocreado.html")

def registro(request):
   return render(request , "formulario_registro.html")

def sesion(request):
   return render(request , "sesion.html")

def agregaral_carrito(request, id):
    # Obtener el producto utilizando el ID proporcionado
    producto = Vender.objects.get(id=id)
        # Crear una instancia de ProductoEnCarrito con los datos del producto
    producto_en_carrito = ProductoEnCarrito(
        Articulo=producto.Articulo,
        Descripcion=producto.Descripcion,
        Precio=producto.Precio
    )
    # Guardar la instancia en la base de datos
    producto_en_carrito.save()
    # Pasar el producto al contexto de la vista
    context = {'producto': producto}
    # Renderizar la plantilla y pasar el contexto
    return render(request, 'carrito.html', context)

def mostrar_carrito(request):
    # Obtener todos los objetos ProductoEnCarrito
    productos_en_carrito = ProductoEnCarrito.objects.all()

    # Pasar los objetos al contexto de la plantilla
    context = {'productos_en_carrito': productos_en_carrito}

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'carritocompras.html', context)






   

     












