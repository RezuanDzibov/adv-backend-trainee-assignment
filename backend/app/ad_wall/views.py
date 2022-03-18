from rest_framework import generics, filters

from ad_wall.models import Ad
from ad_wall.serializers import AdListSerializer, AdRetrieveSerializer


class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price", "created_on"]


class AdRetrieveView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()

    def get_serializer_class(self):
        if self.request.GET.get("fields").lower() in ("true", "1"):
            return AdRetrieveSerializer
        return AdListSerializer
