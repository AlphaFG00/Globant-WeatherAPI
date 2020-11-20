from django.urls import path, include
from citiesweather.api.v1.views import cityweathers

urlpatterns = [
    path('weather', cityweathers.as_view())
]