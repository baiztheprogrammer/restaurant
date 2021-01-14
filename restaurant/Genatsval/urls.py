from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('meals',MealViewSet)
router.register('orders',OrderViewSet)


urlpatterns = [
    path('',include(router.urls)),
]