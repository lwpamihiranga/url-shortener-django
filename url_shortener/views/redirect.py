
from django.shortcuts import get_object_or_404, redirect
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from url_shortener.models import ShortenedUrl


class RedirectView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortenedUrl, short_code=short_code)
        url_obj.access_count += 1
        url_obj.save()
        return redirect(url_obj.original_url, permanent=True)
