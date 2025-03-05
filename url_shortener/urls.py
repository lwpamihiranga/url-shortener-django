from django.urls import path

from .views.stats import StatsView
from .views.shorten_url import ShortenUrlView

urlpatterns = [
    # Add your app's URL patterns here
    path('shorten/', ShortenUrlView.as_view(), name="shorten_url"),
    path('stats/<str:short_code>/', StatsView.as_view(), name="stats_url"),
]
