from rest_framework import serializers
from profile_manager.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('provider_name', 'provider_description', 'category_id', 'subcategory_id', 'country_id', 'state_id',
                  'city_id', 'locality_id', 'pin_code', 'landmark', 'address', 'latitude', 'longitude')

