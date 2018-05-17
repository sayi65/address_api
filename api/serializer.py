from rest_framework import serializers
from django_filters import rest_framework as filters

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('zip_code', 'pref', 'city', 'town', 'kana_pref', 'kana_city', 'kana_town')
        #read_only_fields  = ('zip_code', 'pref', 'city', 'town', 'kana_pref', 'kana_city', 'kana_town')