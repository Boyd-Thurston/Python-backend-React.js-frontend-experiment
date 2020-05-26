from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import FruitBowlSerializer 
from .models import FruitBowl

# Create your views here.

class FruitBowlView(viewsets.ModelViewSet):
  serializer_class = FruitBowlSerializer
  queryset = FruitBowl.objects.all()