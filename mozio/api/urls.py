from django.urls import path
from api.views import (
    CreateProviderAPIView, ProviderDetailsAPIView, CreateServiceAreaAPIView,
    ServiceAreaDetailsAPIView, query_service_areas
)

urlpatterns = [
    path(
        'providers/',
        CreateProviderAPIView.as_view(),
        name="provider_create"
    ),
    path(
        'providers/<int:pk>/',
        ProviderDetailsAPIView.as_view(),
        name="provider_update"
    ), 
    path(
        'service-areas/',
        CreateServiceAreaAPIView.as_view(),
        name="service_area_create"
    ),
    path(
        'service-areas/<int:pk>/',
        ServiceAreaDetailsAPIView.as_view(),
        name="service_area_update"
    ), 
    path('query-service-areas/', query_service_areas),
]