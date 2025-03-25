import logging
from django.shortcuts import get_object_or_404
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from url_shortener.serializers.stats_serializer import StatsSerializer
from url_shortener.models import ShortenedUrl

logger = logging.getLogger(__name__)


class StatsView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, short_code):
        logger.info("Received request for stats of short code: %s", short_code)

        url_obj = get_object_or_404(ShortenedUrl, short_code=short_code)
        serializer = StatsSerializer(url_obj)

        logger.info("Returning stats for short code: %s", short_code)
        logger.info("Original URL: %s", url_obj.original_url)
        logger.info("Access Count: %d | Last Accessed: %s",
                    url_obj.access_count, url_obj.last_accessed)
        return Response(serializer.data, status=status.HTTP_200_OK)
