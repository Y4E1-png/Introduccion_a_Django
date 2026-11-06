from rest_framework import serializers
from .models import ProductModel


class ProductSerializer (serializers.ModelSerializer):
  class Meta:
    model = ProductModel
    fields = [
      "title", "price", "description", "color", "seller"
    ]
