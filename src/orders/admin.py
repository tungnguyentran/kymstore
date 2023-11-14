from django.contrib import admin

from .models import Order, OrderProduct


# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderProductInline
    ]

admin.site.register(Order, OrderAdmin)
