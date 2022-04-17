from django.db import models

class Order(models.Model):
    brand_id = models.IntegerField()
    customer_name = models.CharField(max_length=255, blank=True)
    reference = models.CharField(max_length=255, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    price_total = models.DecimalField(max_digits=16, decimal_places=2)

class Delivery(models.Model):
    order = models.ForeignKey(Order, related_name="deliveries", on_delete=models.DO_NOTHING)
    shipped = models.BooleanField(default=False)
 
class Product(models.Model):
    delivery = models.ForeignKey(Delivery, related_name="products", on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField()
