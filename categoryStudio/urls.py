from django.urls import path, include
from .views import CategoryStudioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryStudioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]