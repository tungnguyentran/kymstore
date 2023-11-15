from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Customer


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    model = Customer

    list_display = ['name', 'phone_number', 'address', 'show_facebook', 'show_email', 'order_count']

    def show_email(self, obj):
        return mark_safe(f'<a href="mailto:{obj.email}">{obj.email}</a>')

    show_email.allow_tags = True
    show_email.short_description = "Email"

    def show_facebook(self, obj):
        return mark_safe(f'<a href="{obj.facebook}">{obj.facebook}</a>')

    show_facebook.allow_tags = True
    show_facebook.short_description = "Facebook"

    def order_count(self, obj):
        return obj.order_set.count()


admin.site.register(Customer, CustomerAdmin)
