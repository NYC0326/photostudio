from django.urls import path, include
from .views import AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]