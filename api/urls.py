# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('', include('companies.urls')),
    path('', include('machines.urls'))
]
