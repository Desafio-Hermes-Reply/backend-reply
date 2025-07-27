# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('machines/', include('machines.urls')),
    path('companies/', include('companies.urls'))
]
