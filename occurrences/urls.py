from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OccurrenceViewSet

router = DefaultRouter()
router.register(r'occurrences', OccurrenceViewSet, basename='occurrence')

urlpatterns = [
    path('', include(router.urls)),
]
