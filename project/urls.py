from django.contrib import admin
from django.urls import include, path

from url_shortener.views import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('short/<str:short_code>/', RedirectView.as_view(), name="redirect-url"),
    path("api/", include("url_shortener.urls")),
]
