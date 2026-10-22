from django.db import models

# Create your models here.

class ProductModel (models.Model):
  title = models.TextField(default = "")
  price = models.FloatField(null=True)
  description = models.TextField(default = "")
  seller = models.TextField(default = "")
  color = models.TextField(default = "")
  product_dimensions = models.FloatField(null=True)