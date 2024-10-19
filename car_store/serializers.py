from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['model_name', 'brand']


class CarPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = ['image']


class CarListSerializer(serializers.ModelSerializer):
    car = CarPhotosSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'car_name', 'car', 'price', 'date']


class CarDetailSerializer(serializers.ModelSerializer):
    car = CarPhotosSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


