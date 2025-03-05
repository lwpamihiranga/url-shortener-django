
from django.shortcuts import get_object_or_404
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from url_shortener.serializers import StatsSerializer
from url_shortener.models import ShortenedUrl


class StatsView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortenedUrl, short_code=short_code)
        serializer = StatsSerializer(url_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
