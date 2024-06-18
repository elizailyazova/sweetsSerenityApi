from rest_framework import serializers

from desserts.serializers import DessertSerializer
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    desserts = DessertSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'desserts']
