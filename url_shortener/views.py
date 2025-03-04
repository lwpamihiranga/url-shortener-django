from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ShortenedUrlSerializer
from .models import ShortenedUrl


class ShortenUrlView(APIView):
    def post(self, request):
        original_url = request.data.get("original_url")

        existing_entry = ShortenedUrl.objects.filter(
            original_url=original_url).first()

        print(request.build_absolute_uri)
        if existing_entry:
            return Response(
                {"short_url": request.build_absolute_uri(
                    f"/short/{existing_entry.short_code}/")},
                status=status.HTTP_200_OK
            )

        serializer = ShortenedUrlSerializer(data=request.data)
        if serializer.is_valid():
            url_instance = serializer.save()
            return Response(
                {"short_url": request.build_absolute_uri(
                    f"/short/{url_instance.short_code}/")},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectView(APIView):
    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortenedUrl, short_code=short_code)
        url_obj.access_count += 1
        url_obj.save()
        return redirect(url_obj.original_url)


