from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls


schema_view = get_schema_view(
   openapi.Info(
      title="Sua API",
      default_version='v1',
      description="Documentação interativa da API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="seuemail@exemplo.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('api.urls')),  # seu app da Company, por exemplo

   #path('docs/', include_docs_urls(title='Documentação da API')),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
