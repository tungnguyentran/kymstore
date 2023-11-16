from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, RentingPrice, ProductImage, Brand


# Register your models here.

class RentingPriceInline(admin.TabularInline):
    model = RentingPrice


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'brand', 'sell_price', 'get_renting_prices', 'created', 'modified']
    inlines = [
        RentingPriceInline,
        ProductImageInline
    ]

    def get_renting_prices(self, obj):
        renting_prices = obj.rentingprice_set.all()
        renting_prices_html = ''
        for renting_price in renting_prices:
            renting_prices_html += '<p><strong>{}</strong>: {:20,} VND</p>'.format(
                renting_price.type_of_renting, renting_price.price)
        return mark_safe(renting_prices_html)


class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ['name', 'description', 'image', 'count_product']

    def count_product(self, obj):
        return obj.product_set.count()


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)

