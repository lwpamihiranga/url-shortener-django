from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from url_shortener.serializers import ShortenedUrlSerializer


class ShortenUrlView(APIView):
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        serializer = ShortenedUrlSerializer(data=request.data)
        if serializer.is_valid():
            url_instance = serializer.save()
            return Response(
                {"short_url": request.build_absolute_uri(
                    f"/short/{url_instance.short_code}/")},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
