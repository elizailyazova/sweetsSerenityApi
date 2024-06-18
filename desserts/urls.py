from django.urls import path, include
from . import views as v
from rest_framework.routers import DefaultRouter
from .views import DessertViewSet

router = DefaultRouter()
router.register(r'desserts', DessertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', v.DessertCreateAPIView.as_view()),
    path('all', v.DessertListAPIView.as_view()),
    path('<int:pk>/', v.DessertDetailAPIView.as_view()),
]
