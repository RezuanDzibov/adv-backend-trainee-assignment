from rest_framework import generics, filters

from ad_wall.models import Ad
from ad_wall.serializers import AdListSerializer


class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price", "created_on"]
