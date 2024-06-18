from rest_framework import generics
from . import models as m, serializers as s
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListAPIView(generics.ListAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderCreateSerializer

class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer
