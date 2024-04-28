from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('' , views.casa , name="casa"),
    path('venta' , views.Venta , name="venta"),
    path('lista' , views.Lista , name="lista"),
    path('alta_articulos',views.alta_articulo , name="alta_articulos"),
    #cargar deberia se exclusivo de usuarios logueados
    path('cargar', views.carga , name="carga"),
    path('agregaral_carrito/<int:id>', views.agregaral_carrito , name="agregaral_carrito"),
    path('agregado', views.carrito , name="carrito"),
    path('mostrarcarrito' , views.mostrar_carrito , name="mostrar_carrito"),
    path('borra_articulo/<int:id>',views.borra_articulo, name="borra_articulo"),
    path('login_user' , views.login_user, name="login_user"),
    path('elimina/<int:id>', views.eliminar_de_lista , name='elimina'),
    path('registro' , views.registro , name = 'registro'),
    path('logout' , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path('editar_user', views.editar_user , name='editar_user'),
    path('modificar/<int:id>', views.modificar_articulo , name="Modificare") #url para modificar articulos cuando usuario este logueado
   
   ]
