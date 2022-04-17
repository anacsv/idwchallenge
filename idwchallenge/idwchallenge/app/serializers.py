from cgitb import lookup
from itertools import product
from app.models import Delivery, Order, Product
from rest_framework import serializers

class ProductDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'quantity']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['delivery', 'product_name', 'quantity']

class DeliverySerializer(serializers.ModelSerializer):
    products = ProductDeliverySerializer(many=True, read_only=True)
    class Meta:
        model = Delivery
        fields = ['id','order', 'shipped', 'products']
    
class OrderSerializer(serializers.ModelSerializer):
    deliveries = DeliverySerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'brand_id', 'customer_name', 'reference', 'order_date', 
        'price_total', 'deliveries']

class OrderQtSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    sum = serializers.DecimalField(max_digits=15, decimal_places=2)
