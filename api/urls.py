from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RecipeViewSet

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]