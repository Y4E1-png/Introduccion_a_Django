from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from ecommerce.models import ProductModel
from django.shortcuts import get_object_or_404, redirect
from django.views import View
# Create your views here.

class ProductList (ListView):
  model = ProductModel
  template_name = "ventas/ventas.html"
  context_object_name = "products"


class Carrito (TemplateView):
  template_name = "ventas/carrito.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    carrito = self.request.session.get("carrito", {})
    productos = ProductModel.objects.filter(id__in=carrito.keys()) 

    context["productos_carrito"] = [
      {
        "producto": producto,
        "cantidad": carrito[str(producto.id)],
      }
      for producto in productos
    ]
    return context



class AñadirAlCarrito (View):
  def post(self, request, productId):
    product = get_object_or_404(ProductModel, id = productId)

    carrito = request.session.get("carrito", {})
    product_id_str = str(product.pk)
    carrito[product_id_str] = carrito.get(product_id_str, 0) + 1

    request.session["carrito"] = carrito
    return redirect ("sales:product_list")


class ProcesarPedido(View):
  def post(self, request):
    carrito = request.session.get("carrito", {})

    if not carrito:
      return redirect("sales:carrito")

    request.session["carrito"] = {}
    return render(request, "ventas/pedido_confirmado.html")

  