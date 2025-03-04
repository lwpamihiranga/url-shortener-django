from django.urls import path
from . import views

urlpatterns = [
    # Add your app's URL patterns here
    path('shorten/', views.ShortenUrlView.as_view(), name="shorten_url"),
    path('stats/<str:short_code>/', views.StatsView.as_view(), name="stats-url"),
]
