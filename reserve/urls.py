from django.urls import path, include
from .views import ReserveViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ReserveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]