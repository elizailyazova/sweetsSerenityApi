from django.urls import path, include
from . import views as v

from rest_framework.routers import DefaultRouter
from .views import BranchViewSet

router = DefaultRouter()
router.register(r'branches', BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', v.BranchCreateAPIView.as_view()),
    path('all', v.BranchListAPIView.as_view()),
]

