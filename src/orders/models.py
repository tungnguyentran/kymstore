from django.db import models

from customers.models import Customer
from products.models import Product


# Create your models here.

class Order(models.Model):

    ORDER_STATUSES = (
        (0, 'Đang chờ'),
        (1, 'Đã xác nhận'),
        (2, 'Đang giao'),
        (3, 'Đã giao'),
        (4, 'Đã hủy'),
    )

    ORDER_TYPES = (
        (0, 'Thuê'),
        (1, 'Mua'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=ORDER_STATUSES[0][0], choices=ORDER_STATUSES)
    type = models.SmallIntegerField(default=ORDER_TYPES[0][0], choices=ORDER_TYPES)
    created = models.DateTimeField(auto_now=True, auto_created=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Order {} - {}".format(str(self.id), self.customer.name)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
