from rest_framework import generics, filters, response, status

from ad_wall.models import Ad
from ad_wall import serializers


class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = serializers.AdListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price", "created_on"]


class AdRetrieveView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()

    def get_serializer_class(self):
        if self.request.GET.get("fields").lower() in ("true", "1"):
            return serializers.AdRetrieveSerializer
        return serializers.AdListSerializer


class AdCreateView(generics.CreateAPIView):
    serializer_class = serializers.AdCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = Ad.objects.create(**serializer.data)
        headers = self.get_success_headers(serializer.data)
        return response.Response(instance.id, status=status.HTTP_201_CREATED, headers=headers)
