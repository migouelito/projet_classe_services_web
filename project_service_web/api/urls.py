from django.urls import path, include
from rest_framework import routers
from .views import CoursViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)  
router.register(r'cours', CoursViewSet)

urlpatterns = [
    path('', include(router.urls)),
]