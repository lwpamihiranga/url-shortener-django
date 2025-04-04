from django.contrib import admin
from django.urls import include, path

from url_shortener.views.redirect import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('short/<str:short_code>/', RedirectView.as_view(), name="redirect_url"),
    path("api/", include("url_shortener.urls")),
]
