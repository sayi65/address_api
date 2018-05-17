from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
import django_filters

from .models import Address
from .serializer import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
  queryset = Address.objects.all();
  serializer_class = AddressSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields  = ('zip_code', 'pref', 'city', 'town', 'kana_pref', 'kana_city', 'kana_town',)
  
