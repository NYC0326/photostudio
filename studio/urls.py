from django.urls import path, include
from .views import StudioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]