from product.models import Product
from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = [
      "id", "name", "description", "price"
    ]


class RegistrationSerializer (ModelSerializer):
  password2 = CharField (
    style = {"input_type":"password"}, write_only = True
  )

  class Meta:
    model = User 
    fields = [
      "username", "email", "password", "password2"
    ]
    extra_kwargs = {
      "password":{"write_only":True}
    }

  def save (self):
    password = self.validated_data ["password"]
    password2 = self.validated_data ["password2"]

    if password != password2 :
      raise ValidationError ({"error": "Ambas contraseñas deben ser iguales"})

    email = self.validated_data ["email"]

    if User.objects.filter (email=email).exists():
      raise ValidationError ({"error": "Este correo ya existe"})

    username = self.validated_data ["username"]

    account = User (email=email, username=username)
    account.set_password (password)
    account.save()

    return account


class UserProfileSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "username", "email"]