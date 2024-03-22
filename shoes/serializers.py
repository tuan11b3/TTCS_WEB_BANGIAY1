from rest_framework import serializers
from .models import Product


class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'discount', 'details', 'gender_id', 'brand_id')