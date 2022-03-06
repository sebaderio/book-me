from rest_framework import serializers as rest_serializers

from barber import models


class ServiceOfferListSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.ServiceOffer
        fields = ('barber_name', 'city', 'id', 'price', 'thumbnail')


class ServiceOfferSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = models.ServiceOffer
        exclude = ('author', 'created_at', 'image', 'status', 'updated_at')