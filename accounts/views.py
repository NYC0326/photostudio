from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets

# 유저 정보 조회
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer