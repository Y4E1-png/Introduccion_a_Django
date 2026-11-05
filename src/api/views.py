from django.shortcuts import render
from rest_framework import views 
from rest_framework.response import Response


class ProductApiView (views.APIView):

  def get (self, request):
    content = {
      "Estas llamando al metodo GET"
    }
    return Response(content)

  def post (self, request):
    content = {
      "Estas llamando al metodo POST"
    }
    return Response(content)

  def put (self, request):
    content = {
      "Estas llamando al metodo PUT"
    } 
    return Response(content)

  def patch (self, request):
    content = {
      "Estas llamando al metodo PATCH"
    }
    return Response(content)

  def delete (self, request):
    content = {
      "Estas llamando al metodo DELETE"
    }
    return Response(content)