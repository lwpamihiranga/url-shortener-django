import logging
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from url_shortener.serializers.url_serializer import ShortenedUrlSerializer

logger = logging.getLogger(__name__)


class ShortenUrlView(APIView):
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        logger.info("Received request to shorten URL: %s", request.data)

        serializer = ShortenedUrlSerializer(data=request.data)
        if serializer.is_valid():
            url_instance = serializer.save()
            short_url = request.build_absolute_uri(
                f"/short/{url_instance.short_code}/")

            logger.info("Successfully created short URL: %s -> %s",
                        url_instance.original_url, short_url)

            return Response({"short_url": short_url},
                            status=status.HTTP_201_CREATED)

        logger.warning("Invalid URL shortening request: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
