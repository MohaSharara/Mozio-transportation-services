from django.contrib.gis.geos import Point

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProviderSerializer, ServiceAreaSerializer
from api.models import Provider, ServiceArea


class CreateProviderAPIView(generics.ListCreateAPIView):
    #An API that shows list of providers and allows adding a new one
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    #An API that shows a certain provider allows edditing or deleting it
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class CreateServiceAreaAPIView(generics.ListCreateAPIView):
    #An API that shows list of service areas and allows adding a new one
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    #An API that shows a certain service area allows edditing or deleting it
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


@api_view(['GET', ])
def query_service_areas(request):
    """
    query service areas function takes latitude and longtitude as parameters
    and then returns a list of all polygons (service areas) that include the given lat/lng
    """
    lng = request.query_params.get("lng") or 0
    lat = request.query_params.get("lat") or 0
    point = Point(float(lng), float(lat))
    service_areas = ServiceArea.objects.all()
    data = []
    
    for service_area in service_areas:
        if point.within(service_area.information):
            data.append({
                "Service Area Name": service_area.name,
                "Provider Name": service_area.provider.name,
                "Price": service_area.price,
                })

    return Response(data)