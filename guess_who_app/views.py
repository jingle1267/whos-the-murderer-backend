from django.shortcuts import render

from .models import User, Image, Clue
from .serializers import UserSerializer, ImageSerializer, ClueSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class ImageViewSet(viewsets.ModelViewSet):
  queryset = Image.objects.all()
  serializer_class = ImageSerializer

class ClueViewSet(viewsets.ModelViewSet):
  queryset = Clue.objects.all()
  serializer_class = ClueSerializer