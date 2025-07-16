from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndustriaViewSet

router = DefaultRouter()
router.register(r'', IndustriaViewSet)  # /api/industrias/

urlpatterns = [
    path('', include(router.urls)),
]
