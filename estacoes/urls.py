from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstacaoTrabalhoViewSet

router = DefaultRouter()
router.register(r'', EstacaoTrabalhoViewSet)  # /api/estacoes/

urlpatterns = [
    path('', include(router.urls)),
]
