from rest_framework import generics, permissions, status, response as res

from desserts.models import Dessert
from desserts.serializers import DessertSerializer
from . import models as m, serializers as s
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer


class DessertByCategoryAPIView(generics.ListAPIView):
    serializer_class = DessertSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Dessert.objects.filter(category_id=category_id)
