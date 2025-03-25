import logging
from django.shortcuts import get_object_or_404, redirect
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from url_shortener.models import ShortenedUrl

logger = logging.getLogger(__name__)


class RedirectView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, short_code):
        logger.info("Received request to redirect short code: %s", short_code)

        url_obj = get_object_or_404(ShortenedUrl, short_code=short_code)
        logger.info("Short code %s found, redirecting to %s",
                    short_code, url_obj.original_url)

        url_obj.access_count += 1
        url_obj.save()
        logger.info("Updated access count for %sshort_code} to %d",
                    short_code, url_obj.access_count)

        return redirect(url_obj.original_url, permanent=True)
