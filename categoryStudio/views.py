from django.shortcuts import render
from rest_framework import viewsets
from .models import CategoryStudio
from .serializers import CategoryStudioSerializer

class CategoryStudioViewSet(viewsets.ModelViewSet):
    queryset = CategoryStudio.objects.all()
    serializer_class = CategoryStudioSerializer