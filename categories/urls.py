from django.urls import path, include
from . import views as v

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', v.CategoryCreateAPIView.as_view()),
    path('all', v.CategoryListAPIView.as_view()),
    path('<int:pk>/', v.CategoryDetailAPIView.as_view()),
    path('dessert/<int:category_id>/', v.DessertByCategoryAPIView.as_view()),
    path('', include(router.urls)),
]
