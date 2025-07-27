# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('companies/', include('companies.urls'))
]
