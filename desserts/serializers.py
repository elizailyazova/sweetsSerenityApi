from rest_framework import serializers
from .models import Dessert

class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ['id', 'name', 'category', 'price', 'image', 'description', 'formula', 'nutrition', 'calories', 'freshness_date']


