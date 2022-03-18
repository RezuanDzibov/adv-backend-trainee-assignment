from rest_framework import generics, filters, response, status

from ad_wall.models import Ad, Image
from ad_wall import serializers


class AdListView(generics.ListAPIView):
    """
    Retrieve list of ads.
    """
    queryset = Ad.objects.all()
    serializer_class = serializers.AdListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price", "created_on"]


class AdRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve an ad by id.
    """
    queryset = Ad.objects.all()

    def get_serializer_class(self):
        if self.request.GET.get("fields").lower() in ("true", "1"):
            return serializers.AdRetrieveSerializer
        return serializers.AdListSerializer


class AdCreateView(generics.CreateAPIView):
    serializer_class = serializers.AdCreateSerializerWithImages

    def post(self, request, *args, **kwargs):
        """
        Create a new ad with the given images
        
        :param request: The request that was sent to the API view
        :return: The id of the newly created ad.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        images = serializer.data.get("images", None)
        serializer = serializers.AdCreateSerializer(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        instance = Ad.objects.create(**serializer.data)
        if not images:
            for image in images:
                Image.objects.create(ad=instance, url=image)
        headers = self.get_success_headers(serializer.data)
        return response.Response(instance.id, status=status.HTTP_201_CREATED, headers=headers)
