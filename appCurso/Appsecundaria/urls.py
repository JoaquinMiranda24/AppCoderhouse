from django.urls import path
from . import views

urlpatterns = [
    path('' , views.casa , name="casa"),
    path('venta' , views.Venta , name="venta"),
    path('lista' , views.Lista , name="lista"),
    path('alta_articulos',views.alta_articulo , name="alta_articulos"),
    path('cargar', views.carga , name="carga"),
    path('agregaral_carrito/<int:id>', views.agregaral_carrito , name="agregaral_carrito"),
    path('agregado', views.carrito , name="carrito"),
    path('alta_usuario',views.alta_usuario),
    path('iniciasesion' ,views.sesion , name="iniciasesion"),
    path('registro', views.registro , name="registro"),
    path('mostrarcarrito' , views.mostrar_carrito , name="mostrar_carrito")

    
    
]

