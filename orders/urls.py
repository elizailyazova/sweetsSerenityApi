from django.urls import path, include
from . import views as v

from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', v.OrderCreateAPIView.as_view()),
    path('all/', v.OrderListAPIView.as_view()),
    path('<int:pk>/', v.OrderDetailAPIView.as_view())
]
