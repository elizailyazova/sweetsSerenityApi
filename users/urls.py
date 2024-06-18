from django.urls import path, include
from . import views as v
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', v.RegisterAPIView.as_view()),
    path('login', v.LoginAPIView.as_view()),
    path('logout', v.LogoutAPIView.as_view()),
    path('profile/', v.ProfileAPIView.as_view()),
    path('all/', v.UserListAPIView.as_view()),
]
