from django.http import request , HttpResponse
from django.shortcuts import render , redirect
from Appsecundaria.models import Vender , ProductoEnCarrito ,Avatar
from Appsecundaria.forms import vender_articulos , seleccion_articulos , AgregarAlCarritoForm , UserEditForm
from django.template import loader
from django.db.models import Sum
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required #esto hace que para acceder a alguna vista se requiera iniciar sesion primero, con @login_required




 
def casa(request):
    usuario = request.user.username
    productos = Vender.objects.all()
    dicc = {"productos": productos, "usuario": usuario}
    #avatares = Avatar.objects.filter(user=request.user.id)
   
    #return render(request, "home.html", dicc , {"url":avatares[0].imagen.url })
    return render(request, "home.html", dicc )


def Venta(request):

    with open("C:/Users/jotae/OneDrive/Escritorio/appPractica/appCurso/Appsecundaria/templates/formulario_articulos.html") as file:
        formulario_html = file.read()
    return render(request, "formulario_articulos.html")

def Lista(request):
    productos = Vender.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if avatares.exists():  # Verifica si hay avatares disponibles
        url_avatar = avatares[0].imagen.url
    else:
        url_avatar = None  # O cualquier otro valor predeterminado si no hay avatares
    
    return render(request, "lista.html", {"url": url_avatar, "productos": productos})


#cuando se despliegue esta view ,tenemos que agregar el boton editar producto de la lista pero el boton editar solo puede acceder el usuario cuando inicio sesion


def alta_articulo(request):

    if request.method == "POST":
      #llamar a mi formulario creado en forms.py:
        formulario = vender_articulos(request.POST)
        if formulario.is_valid():
           articulo_nuevo = Vender( Articulo = request.POST["Articulo"],Descripcion = request.POST["Descripcion"], Precio = request.POST["Precio"])
           articulo_nuevo.save()
        return render(request , "creado.html")
        
@login_required    
def carga(request):
   return render(request , "formulario_articulos.html")

def carrito(request):
   return render(request , "carrito.html")



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

    # Obtener la suma total de los precios de todos los productos en el carrito
    total_precio = productos_en_carrito.aggregate(total_precio=Sum('Precio'))

    # Pasar los objetos al contexto de la plantilla
    context = {'productos_en_carrito': productos_en_carrito,
               'total_precio': total_precio['total_precio']  # Total de precios en el carrito
    }

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'carritocompras.html', context)



def carrito_lateral(request):

    with open("C:/Users/jotae/OneDrive/Escritorio/appPractica/appCurso/Appsecundaria/templates/carrito_lateral.html") as file:
        indice_html = file.read()
    #pasar el nombre de la plantilla, no el contenido
    return render(request, 'carrito_lateral.html')


def borra_articulo(request, id):
    # Obtener el producto en el carrito por su ID
    producto = ProductoEnCarrito.objects.get(id=id)

    # Eliminar el producto del carrito
    producto.delete()

    # Recalcular el total del precio después de eliminar el artículo
    total_precio = ProductoEnCarrito.objects.aggregate(total_precio=Sum('Precio'))

    # Obtener todos los productos restantes en el carrito
    productos_en_carrito = ProductoEnCarrito.objects.all()

    # Pasar los objetos y el total del precio al contexto de la plantilla
    context = {
        'productos_en_carrito': productos_en_carrito,
        'total_precio': total_precio['total_precio']  # Total de precios en el carrito
    }

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'carritocompras.html', context)

def login_user(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user =  authenticate(username = usuario , password = contra)

            #usuario = joaco
            #contra = wsaenotsock123

            if user is not None:

                login(request , user)
                
                
                #esta linea se agrego para subir el avatar en la ultima clase:
                avatares = Avatar.objects.filter(user=request.user.id)

                return render(request , "home.html", {"url":avatares[0].imagen.url })
                                                               
            else:
                return(HttpResponse(f"usuario no encontrado"))
        else:

            return HttpResponse(f"form incorrecto {form}")
        
    form = AuthenticationForm()
    return render (request , "panelsesion.html" , {"form": form})

#seguiria la parte de usercreationform 1 hora 30
#de la ultima clase 1 hora 50 minutos explica la entrega final, es sencilla : hacer funcionar el avatar, CRUD para todos los modelos, login y logout


def eliminar_de_lista(request , id):

    #funcion que permite al usuario logueado eliminar productos de la lista

    # Obtener el producto por su ID
    producto = Vender.objects.get(id=id)

    # Eliminar el producto del carrito
    producto.delete()

    producto = Vender.objects.all()

    # Pasar los objetos y el total del precio al contexto de la plantilla
    context = {
       'producto' : producto
       }

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'lista.html', context)

def registro(request):

        if request.method == "POST":
          
          form = UserCreationForm(request.POST)

          if form.is_valid():
              form.save()
              #return HttpResponse("usuario creado")
              return render(request , "usuariocreado.html")

        else:
          
            form = UserCreationForm()

        return render(request , "formulario_registro.html" , {"form":form})


#repasar ultima clase agregar avatar 1 hora 44

def editar_user(request):

    usuario = request.user
    
    if request.method == "POST":
      
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion =miFormulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "padre.html")

    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario": usuario})


   

     












