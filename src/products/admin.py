from django.contrib import admin

from .models import Product, RentingPrice, ProductImage, Brand


# Register your models here.

class RentingPriceInline(admin.TabularInline):
    model = RentingPrice


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'brand', 'sell_price', 'created', 'modified']
    inlines = [
        RentingPriceInline,
        ProductImageInline
    ]


class BrandAdmin(admin.ModelAdmin):
    model = Brand


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)

