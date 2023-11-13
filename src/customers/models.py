from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20)
    facebook = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150, null=True)
