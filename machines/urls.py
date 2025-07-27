# machines/urls.py
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet

router = DefaultRouter()
router.register(r'machines', MachineViewSet, basename='machine')

urlpatterns = router.urls
