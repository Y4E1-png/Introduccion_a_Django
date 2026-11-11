from django.shortcuts import get_object_or_404
from rest_framework import views 
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from product.models import Product
from .serializer import ProductSerializer, RegistrationSerializer, UserProfileSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated



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


class TestViewSet (ViewSet):

  serializer_class = ProductSerializer 

  def list (self, request):
    productos = Product.objects.all()
    serializer = self.serializer_class(productos, many=True)

    return Response (serializer.data)


  def create (self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data, status= status.HTTP_201_CREATED)
    else:
      return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)


  def retrieve (self, request, pk=None):
    producto = get_object_or_404(Product, pk=pk)
    serializer = self.serializer_class(producto)
    return Response (serializer.data)


  def update (self, request, pk=None):
    producto = get_object_or_404(Product, pk=pk)
    serializer = self.serializer_class(producto,data=request.data )

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data)
    else:
      return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)


  def partial_update(self, request, pk=None):
    producto = get_object_or_404(Product, pk=pk)
    serializer = self.serializer_class(producto, data=request.data, partial=True)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def destroy(self, request, pk=None):
    producto = get_object_or_404(Product, pk=pk)
    producto.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view (["POST"])
def registration_view (request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
      account = serializer.save()
      refresh = RefreshToken.for_user(account)

      return Response ({
        "response":"Resgitro Exitoso",
        "username": account.username,
        "email": account.email,
        "token": {
          "refresh":str(refresh),
          "access":str(refresh.access_token)
        }
      }, status=status.HTTP_201_CREATED)
    else:
      return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView (views.APIView):
  permission_classes = [IsAuthenticated]

  def get (self, request):
    serializer = UserProfileSerializer(request.user)
    return Response (serializer.data)