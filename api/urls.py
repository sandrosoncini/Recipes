from django.urls import path
from rest_framework import routers
from django.conf.urls import include

router = routers.DefatultRouter()

urlpatterns = [
    path('', include(router.urls)),
]