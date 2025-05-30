import logging
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from url_shortener.models import ShortenedUrl

logging.disable(logging.WARNING)


class ShortenUrlViewTests(APITestCase):

    def test_shorten_url_success(self):
        url = reverse("shorten_url")
        data = {"original_url": "http://example.com/"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("short_url", response.data)

    def test_invalid_url(self):
        url = reverse("shorten_url")
        data = {"original_url": "invalid_url"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_custom_short_code_success(self):
        custom_short_code = "testcode"

        url = reverse("shorten_url")
        data = {"original_url": "http://example.com/",
                "short_code": custom_short_code}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("short_url", response.data)
        self.assertEqual(response.data["short_url"].split(
            "short/")[1], f"{custom_short_code}/")

    def test_existing_custom_short_code(self):
        custom_short_code = "testcode"

        ShortenedUrl.objects.create(
            original_url="http://example.com/",
            short_code=custom_short_code,
        )

        url = reverse("shorten_url")
        data = {"original_url": "http://example.com/",
                "short_code": custom_short_code}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


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

        self.assertEqual(response.status_code,
                         status.HTTP_301_MOVED_PERMANENTLY)
        self.assertEqual(response.url, "http://example.com/")

        self.shortned_url.refresh_from_db()
        self.assertEqual(self.shortned_url.access_count, 1)

    def test_redirect_invalid_short_code(self):
        url = reverse("redirect_url", kwargs={"short_code": "nothing"})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class StatsViewTests(APITestCase):

    def setUp(self):
        self.shortned_url = ShortenedUrl.objects.create(
            original_url="http://example.com/",
            short_code="aabbcc",
            access_count=5,
        )

    def test_get_stats_success(self):
        url = reverse("stats_url", kwargs={"short_code": "aabbcc"})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["short_code"], "aabbcc")
        self.assertEqual(response.data["access_count"], 5)
        self.assertIn("last_accessed", response.data)

    def test_get_stats_not_found(self):
        url = reverse("stats_url", kwargs={"short_code": "nothing"})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
