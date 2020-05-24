from django.contrib import admin
from .models import FruitBowl

class FruitBowlAdmin(admin.ModelAdmin):
  list_display = ('fruit','url', 'visable')

# Register your models here.
admin.site.register(FruitBowl, FruitBowlAdmin)