import hashlib
import base64

from django.db import models


def generate_short_code(url):
    """Generate the short code for the URL"""

    hash_digest = hashlib.sha256(url.encode()).digest()
    short_code = base64.urlsafe_b64encode(hash_digest)[:6].decode("utf-8")

    counter = 1
    while ShortenedUrl.objects.filter(short_code=short_code).exists():
        short_code = base64.urlsafe_b64encode(
            hash_digest)[:5].decode("utf-8") + str(counter)
        counter += 1

    return short_code


class ShortenedUrl(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField(unique=False)
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    access_count = models.PositiveIntegerField(default=0)
    last_accessed = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code(self.original_url)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
