from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import ProductModel
from .forms import ProductModelForm
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.


def detail_view(request, product_id):
  objeto = get_object_or_404(ProductModel, id = product_id)

  context = {
    "product" : objeto
  }
  template = "ecommerce/detail-view.html"
  return render (request, template, context)


def list_view (request):
  query = request.GET.get ("q", None)
  queryset = ProductModel.objects.all()
  if query is not None:
    queryset = queryset.filter(
      Q(title__icontains = query) 
    )
  template = "ecommerce/list-view.html"
  context = {
    "products" : queryset
  }
  return render (request, template, context)


def create_view(request):
  form = ProductModelForm (request.POST or None)
  if form.is_valid():
    objeto = form.save (commit=False)
    objeto.save()
    messages.success (request, "Producto creado con exito")
    return HttpResponseRedirect ("/ecommerce/{product_id}".format(product_id = objeto.id))
  context = {
    "form": form
  }
  template = "ecommerce/create-view.html"
  return render (request, template, context)


def update_view (request, product_id=None):
  objeto = get_object_or_404 (ProductModel, id = product_id)
  form = ProductModelForm (request.POST or None, instance = objeto)
  if form.is_valid():
    objeto = form.save(commit = False)
    objeto.save()
    messages.success (request, "Producto actualizado con exito")
    return HttpResponseRedirect ("/ecommerce/{product_id}".format(product_id = objeto.id))
  context = {
    "form":form
  }
  template = "ecommerce/update-view.html"
  return render (request, template, context)


def delete_view (request, product_id):
  objeto = get_object_or_404 (ProductModel, id = product_id)
  if request.method == "POST":
    objeto.delete()
    messages.success (request, "Articulo eliminado con exito")
    return HttpResponseRedirect ("/ecommerce/")

  context = {
    "product":objeto
  }

  template = "ecommerce/delete-view.html"
  return render (request, template, context)
  