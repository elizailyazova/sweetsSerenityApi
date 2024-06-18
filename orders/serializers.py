from rest_framework import serializers

from desserts.serializers import DessertSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(source='dessert.number', read_only=True)
    dessert_name = serializers.CharField(source='dessert.name', read_only=True)
    dessert_price = serializers.DecimalField(source='dessert.price', max_digits=10, decimal_places=2, read_only=True)
    dessert_image = serializers.ImageField(source='dessert.image', read_only=True)

    class Meta:
        model = Order
        fields = ['number', 'dessert_name', 'dessert_price', 'dessert_image', 'user', 'quantity', 'branch']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['number', 'user', 'dessert', 'quantity', 'branch']


class OrderDetailSerializer(serializers.ModelSerializer):
    dessert = DessertSerializer()

    class Meta:
        model = Order
        fields = ['number', 'user', 'dessert', 'quantity', 'branch']
