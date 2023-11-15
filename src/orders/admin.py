from django.contrib import admin
from django.db.models import Count

from .models import Order, OrderProduct


# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product_count', 'status', 'created', 'modified']
    inlines = [
        OrderProductInline
    ]

    def product_count(self, obj):
        return obj.orderproduct_set.count()


admin.site.register(Order, OrderAdmin)
