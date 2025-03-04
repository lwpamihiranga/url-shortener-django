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


class RedirectViewTests(APITestCase):
    def setUp(self):
        self.shortned_url = ShortenedUrl.objects.create(
            original_url="http://example.com/",
            short_code="aabbcc",
            access_count=0,
        )

    def test_redirect_valid_short_code(self):
        url = reverse("redirect_url", kwargs={"short_code": "aabbcc"})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, "http://example.com/")

        self.shortned_url.refresh_from_db()
        self.assertEqual(self.shortned_url.access_count, 1)

    def test_redirect_invalid_short_code(self):
        url = reverse("redirect_url", kwargs={"short_code": "nothing"})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

