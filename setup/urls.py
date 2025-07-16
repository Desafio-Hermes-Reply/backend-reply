from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from login.views import register, user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user-info/', user_info, name='user_info'),
    path('api/industrias/', include('industrias.urls')),
    path('api/estacoes/', include('estacoes.urls')),
    path('api/maquinas/', include('maquinas.urls')),

]
