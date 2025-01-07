from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
custom_router = DefaultRouter()
custom_router.register(r'items', ItemViewSet, basename='item')

urlpatterns = custom_router.urls
