from django.urls import path, re_path

from .views.stats import StatsView
from .views.shorten_url import ShortenUrlView
from .views.not_implemented import NotImplementedView

urlpatterns = [
    path('shorten/', ShortenUrlView.as_view(), name="shorten_url"),
    path('stats/<str:short_code>/', StatsView.as_view(), name="stats_url"),
    re_path(r'^.*$', NotImplementedView.as_view()),
]
