from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
import json
from datetime import datetime
from rest_framework import status
import os


class cityweather(APIView, ):
    permission_classes = (AllowAny,)
    def get(self, request):
        is_valid = self.validate(request)
        if is_valid != True:
            return is_valid
        params = {"q": f'{request.query_params["city"]}, {request.query_params["country"]}'}
        response = self.get_weather_api_response(params)
        if response['cod'] != 200:
            return Response(status=response['cod'], data=response['message'])
        else:
            return Response({
                    "location_name":    f'{response["name"]}{", "}{response["sys"]["country"]}',
                    "temperature: ":    f'{int(response["main"]["temp"]-273.15)}{"°C"}',
                    "wind :":           f'{response["weather"][0]["main"]}{", "}{response["wind"]["speed"]}{" m/s"}',
                    "cloudiness:":      f'{response["weather"][0]["description"]}',
                    "pressure: ":       f'{response["main"]["pressure"]}{" hpa"}',
                    "humidity: ":       f'{response["main"]["humidity"]}{"%"}',
                    "sunrise:":         datetime.fromtimestamp(response['sys']['sunrise']).time(),
                    "sunset: ":         datetime.fromtimestamp(response['sys']['sunset']).time(),
                    "geo_coordinates:": f'[{ response["coord"]["lon"]},{response["coord"]["lat"]}]',
                    "requested_time:":  datetime.now()
                })

    def validate(self, data):
        city = data.query_params.get('city', None)
        country = data.query_params.get('country', None)
        if city is None or country is None:
            return Response({"status": "required fields not found"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        if len(country) != 2:
            return Response({'status': 'country invalid length'}, status=status.HTTP_400_BAD_REQUEST)
        return True

    def get_weather_api_response(self, params):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        headers = {
            'x-rapidapi-key': os.getenv('X-RAPIDAPI-KEY'),
            'x-rapidapi-host': os.getenv('X-RAPIDAPI-HOST')
        }
        response = requests.request("GET", url, headers=headers, params=params)
        return json.loads(response.text)