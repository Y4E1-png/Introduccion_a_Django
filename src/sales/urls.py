from django.urls import path
from .views import ProductList, AñadirAlCarrito, Carrito, ProcesarPedido

app_name = "sales"

urlpatterns = [
  path("productos/", ProductList.as_view(), name="product_list"),
  path("carrito/agregar/<int:productId>/", AñadirAlCarrito.as_view(), name="añadir_al_carrito"),
  path("carrito/", Carrito.as_view(), name="carrito"),
  path("pedido/procesar/", ProcesarPedido.as_view(), name="procesar_pedido")
]
