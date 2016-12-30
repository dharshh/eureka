from django.db import models

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created At')
    deleted_at = models.DateTimeField('Deleted At')
    modified_at = models.DateTimeField('Modified At')
    modified_by = models.IntegerField(default=1)


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created At')
    deleted_at = models.DateTimeField('Deleted At')
    modified_at = models.DateTimeField('Modified At')
    modified_by = models.IntegerField(default=1)


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created At')
    deleted_at = models.DateTimeField('Deleted At')
    modified_at = models.DateTimeField('Modified At')
    modified_by = models.IntegerField(default=1)


class Locality(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    locality_name = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created At')
    deleted_at = models.DateTimeField('Deleted At')
    modified_at = models.DateTimeField('Modified At')
    modified_by = models.IntegerField(default=1)


class Provider(models.Model):
    provider_name = models.CharField(max_length=50)
    provider_description = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country)
    state_id = models.ForeignKey(State)
    city_id = models.ForeignKey(City)
    locality_id = models.ForeignKey(Locality)
    pin_code = models.IntegerField(default=0)
    landmark = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    created_at = models.DateTimeField('Created At')
    deleted_at = models.DateTimeField('Deleted At')
    modified_at = models.DateTimeField('Modified At')
    modified_by = models.IntegerField(default=1)


class Item(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=50)
    category_id = models.IntegerField(default=None)
    sub_category_id = models.IntegerField(default=None)
    price = models.IntegerField(default=0)
    available_quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField('Created At')
    deleted_at = models.DateTimeField('Deleted At')
    modified_at = models.DateTimeField('Modified At')
    modified_by = models.IntegerField(default=1)
