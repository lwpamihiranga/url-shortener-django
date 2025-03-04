from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import ShortenedUrl


class ShortenUrlViewTests(APITestCase):

    def test_shorten_url_success(self):
        url = reverse("shorten_url")
        data = {"original_url": "http://example.com/"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("short_url", response.data)

    def test_duplicate_url(self):
        ShortenedUrl.objects.create(
            original_url="http://example.com/", short_code="aabbcc")

        url = reverse("shorten_url")
        data = {"original_url": "http://example.com/"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

