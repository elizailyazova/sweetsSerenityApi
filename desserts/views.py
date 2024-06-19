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
    if request.method == 'GET':
        query = request.GET.get('dessertName', '')
        if query:
            desserts = Dessert.objects.filter(name__icontains=query)
        else:
            desserts = Dessert.objects.all()

        desserts_json = serializers.serialize('json', desserts)
        return JsonResponse(desserts_json, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
