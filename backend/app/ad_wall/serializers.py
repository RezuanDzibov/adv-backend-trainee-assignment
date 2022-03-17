from rest_framework import serializers

from .models import Ad


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            "name",
            "primary_image_url",
            "price",
        )
