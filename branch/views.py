from rest_framework import generics, permissions, status, response as res

from . import models as m, serializers as s
from rest_framework import viewsets
from .models import Branch
from .serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchCreateAPIView(generics.ListCreateAPIView):
    queryset = m.Branch.objects.all()
    serializer_class = s.BranchSerializer


class BranchListAPIView(generics.ListAPIView):
    queryset = m.Branch.objects.all()
    serializer_class = s.BranchSerializer
