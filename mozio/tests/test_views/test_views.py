import pytest

from model_bakery import baker
from django.urls import reverse
from django.contrib.gis.geos import Point


@pytest.mark.django_db(True)
def test_provider_view(client):
   #Testing if porvider create/list view link works
   url = reverse('provider_create')
   response = client.get(url)
   assert response.status_code == 200


@pytest.fixture
def provider():
   #Creating a provider with id=2
   return baker.make('api.Provider', id=2)


@pytest.mark.django_db(True)
def test_provider_get_view(client, provider):
   #Testing if porvider retrieve/update view link works
   url = reverse('provider_update', kwargs={'pk': provider.id})
   response = client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db(True)
def test_service_area_view(client):
   #Testing if service area create/list view link works
   url = reverse('service_area_create')
   response = client.get(url)
   assert response.status_code == 200


@pytest.fixture
def service_area():
   #Creating a service area with information to test in query
   return baker.make(
      'api.ServiceArea',
      id=1,
      information="SRID=4326;POLYGON ((11.102371215820312 46.21939582902924,"\
         "11.106491088867188 46.22111800038881, 11.134214401245117 46.22188999070486,"\
         "11.140050888061523 46.21791115519151, 11.141080856323242 46.21422899084459,"\
         "11.137990951538086 46.207695510993354, 11.13412857055664 46.20122065978115,"\
         "11.12485885620117 46.198844376182535, 11.102371215820312 46.21939582902924))"
   )


@pytest.mark.django_db(True)
def test_service_area_get_view(client, service_area):
   #Testing if service area retrieve/update view link works
   url = reverse('service_area_update', kwargs={'pk': service_area.id})
   response = client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db(True)
def test_query(service_area):
   #Test if query for a point inside a service area workss
   point = Point(11.1245718, 46.2071762)
   assert point.within(service_area.information) == True
