from django.db import models
from django.conf import settings


# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(settings.MEDIA_ROOT)


class Product(models.Model):
    SIZE_XS = "XS"
    SIZE_S = "X"
    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"
    SIZE_CHOICES = (
        (SIZE_XS, SIZE_XS),
        (SIZE_S, SIZE_S),
        (SIZE_M, SIZE_M),
        (SIZE_L, SIZE_L),
        (SIZE_XL, SIZE_XL)
    )

    CONDITION_NEW_TAG = "New Tag"
    CONDITION_USED = "Used"
    CONDITION_LIKE_NEW = "Like new"
    CONDITION_OLD = "Old"
    CONDITION_CHOICES = (
        (CONDITION_NEW_TAG, CONDITION_NEW_TAG),
        (CONDITION_USED, CONDITION_USED),
        (CONDITION_LIKE_NEW, CONDITION_LIKE_NEW),
        (CONDITION_OLD, CONDITION_OLD)
    )

    DEFAULT_COLOR = "Trắng"

    STATUS_READY_FOR_RENT = "Ready for renting"
    STATUS_BEING_RENTED = "Being rented"
    STATUS_WASHING = "Washing"

    STATUS_CHOICES = (
        (0, STATUS_READY_FOR_RENT),
        (1, STATUS_BEING_RENTED),
        (2, STATUS_WASHING)
    )

    product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default=SIZE_XS)
    color = models.CharField(max_length=100, default=DEFAULT_COLOR)
    condition = models.CharField(max_length=20, default=CONDITION_NEW_TAG)
    original_price = models.IntegerField(default=0)
    bought_price = models.IntegerField(default=0)
    status = models.SmallIntegerField(default=STATUS_CHOICES[0][0])
    bought_date_time = models.DateTimeField(null=True)
    sell_price = models.IntegerField(default=0)


class RentingPrice(models.Model):
    ONE_DAY = "1 Ngày"
    THREE_DAYS = "3 Ngày"

    TYPE_RENTING_CHOICES = (
        (ONE_DAY, ONE_DAY),
        (THREE_DAYS, THREE_DAYS)
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_of_renting = models.CharField(max_length=20, choices=TYPE_RENTING_CHOICES, default=ONE_DAY)
    price = models.IntegerField(default=0)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d')
