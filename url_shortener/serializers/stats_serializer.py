
from rest_framework import serializers
from url_shortener.models import ShortenedUrl


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = ["original_url", "short_code",
                  "access_count", "last_accessed"]
