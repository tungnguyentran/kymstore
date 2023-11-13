from django.db import models

from customers.models import Customer
from products.models import Product


# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now=True, auto_created=True)
    modified = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
