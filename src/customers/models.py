from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Customer(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Nhập đúng format số điện thoại")
    url_regex = RegexValidator(
        regex=r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/\S*)?$', message="Nhập đúng format url")

    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=20)
    facebook = models.CharField(max_length=100, null=True, validators=[url_regex])
    address = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name