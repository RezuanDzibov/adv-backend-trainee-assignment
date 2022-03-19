from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter
from rest_framework import filters, generics, response, status
from rest_framework.serializers import Serializer

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

    @swagger_auto_schema(
        manual_parameters=[
            Parameter(
                name="fields",
                in_="query",
                type="boolean",
                required=False,
                description="If the parameter is true then all fields of the object will return",
            ),
        ],
    )
    def get(self, request, *args, **kwargs) -> response.Response:
        return super().get(request, *args, **kwargs)

    def get_serializer_class(self) -> Serializer:
        is_fields = self.request.GET.get("fields", None)
        if is_fields and is_fields.lower() == "true":
            return serializers.AdRetrieveSerializer
        return serializers.AdListSerializer


class AdCreateView(generics.CreateAPIView):
    serializer_class = serializers.AdCreateSerializerWithImages

    def post(self, request, *args, **kwargs) -> response.Response:
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
        return response.Response(
            instance.id,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
