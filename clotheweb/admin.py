from django.contrib import admin
from .models import Product, Cart, Order, CartDescription,ContactQuery
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartDescription)  # Assuming CartDescription is a model you want to register
admin.site.register(ContactQuery)