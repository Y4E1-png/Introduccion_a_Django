from django.db import models
from address.models import Address
# Create your models here.


class BillingProfile (models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  address = models.ForeignKey(Address, on_delete=models.CASCADE)

  