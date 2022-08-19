from django.shortcuts import render
from rest_framework import viewsets
from .models import Studio
from .serializers import StudioSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer