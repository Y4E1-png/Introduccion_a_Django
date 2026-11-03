from django.db import models
from billing_profile.models import BillingProfile
from address.models import Address
from cart.models import Cart

class Orders (models.Model):
  billing_profile = models.ForeignKey(BillingProfile, null = True, blank = True, on_delete=models.CASCADE)
  order_id = models.CharField(max_length=120, blank= True)
  shipping_address = models.ForeignKey(Address, related_name="shipping_address", null=True, blank=True, on_delete=models.CASCADE)
  billing_adrress = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True, on_delete=models.CASCADE)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  status = models.CharField (max_length=120, default="created")
  shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
  total = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
  active = models.BooleanField(default=True)
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)


