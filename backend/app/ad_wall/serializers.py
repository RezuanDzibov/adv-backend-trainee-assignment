from rest_framework import serializers

from .models import Ad


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            "id",
            "name",
            "primary_image_url",
            "price",
        )


class ImageListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.url


class AdRetrieveSerializer(serializers.ModelSerializer):
    images = ImageListingField(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = (
            "id",
            "name",
            "description",
            "price",
            "created_on",
            "primary_image_url",
            "images",
        )
