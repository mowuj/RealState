from rest_framework import serializers
from .models import *
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=('title','slug',
                'photo','bedrooms',
                'bathrooms','sqft',
                'city','state',
                'zipcode','address',
                'sale_type','home_type',
                'price')

class HomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields='__all__'
        lookup_field='slug'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageFiles
        fields='__all__'
        lookup_field='home'