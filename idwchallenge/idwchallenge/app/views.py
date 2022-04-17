from rest_framework import viewsets, permissions
from app.serializers import OrderSerializer, DeliverySerializer, ProductSerializer, OrderQtSerializer
from app.models import Delivery, Order, Product
from django.db.models import Sum

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        brand_id = self.request.query_params.get('brand_id', None)
        if brand_id is not None:
            self.queryset = self.queryset.filter(brand_id=brand_id)
        return self.queryset

class OrderQtViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.values('product_name').annotate(sum=Sum('quantity'))
    serializer_class = OrderQtSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        order_id = self.request.query_params.get('order_id', None)
        if order_id is not None:
            self.queryset = self.queryset.filter(delivery__order__id=order_id)

        reference = self.request.query_params.get('reference', None)
        if reference is not None:
            self.queryset = self.queryset.filter(delivery__order__reference__iexact=reference)

        return self.queryset


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]