from django.contrib import admin
from .models import Order, Delivery, Product

admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Product)