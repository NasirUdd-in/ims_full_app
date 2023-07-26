from django.contrib import admin
from .models import (
    Supplier,
    Customers,
    Product,
    Purchase,
    Sale
)
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Sale)