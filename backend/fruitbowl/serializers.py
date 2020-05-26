from rest_framework import serializers
from .models import FruitBowl

class FruitBowlSerializer(serializers.ModelSerializer):
  class Meta:
    model = FruitBowl
    fields = ('id', 'fruit', 'url', 'visable')