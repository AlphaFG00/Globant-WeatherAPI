from django.urls import path, include
from citiesweather.api.v1.views import cityweather

urlpatterns = [
    path('weather', cityweather.as_view())
]