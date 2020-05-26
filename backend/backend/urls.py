    from django.contrib import admin
    from django.urls import path, include
    from rest_framework import routers 
    from fruitbowl import views

    router = routers.DefaultRouter()
    router.register(r'fruitbowl', views.FruitBowlView, 'fruitbowl')

    urlpatterns = [
        path('admin/', admin.site.urls),         path('api/', include(router.urls)) 
    ]
