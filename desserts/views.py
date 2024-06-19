from rest_framework import generics, permissions, status, response as res
from unicodedata import category

from . import models as m, serializers as s
from rest_framework import viewsets
from .serializers import DessertSerializer
from .models import Dessert, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core import serializers


class DessertViewSet(viewsets.ModelViewSet):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer


class DessertCreateAPIView(generics.ListCreateAPIView):
    queryset = m.Dessert.objects.all()
    serializer_class = s.DessertSerializer


class DessertListAPIView(generics.ListAPIView):
    queryset = m.Dessert.objects.all()
    serializer_class = s.DessertSerializer


class DessertDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Dessert.objects.all()
    serializer_class = s.DessertSerializer


def search_desserts(request):
    query = request.GET.get('query', '')
    desserts = Dessert.objects.filter(name__icontains=query)

    data = []
    for dessert in desserts:
        dessert_data = {
            "id": dessert.id,
            "name": dessert.name,
            "category": dessert.category_id,
            "price": str(dessert.price),
            "image": request.build_absolute_uri(dessert.image.url),
            "description": dessert.description,
            "formula": dessert.formula,
            "nutrition": dessert.nutrition,
            "calories": dessert.calories,
            "freshness_date": dessert.freshness_date
        }
        data.append(dessert_data)

    return JsonResponse(data, safe=False)
