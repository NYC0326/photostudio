from django.shortcuts import render
from rest_framework import viewsets
from reserve.serializers import ReserveSerializer
from .models import Reserve

# Create your views here.
class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer