
from rest_framework import serializers
from url_shortener.models import ShortenedUrl


class ShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = ["original_url", "short_code"]
