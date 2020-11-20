from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.


class citiesweathertestcase(APITestCase):
    def test_get_weather_ok(self):
        url = "/weather?city=Mexico&country=mx"
        response = self.client.get(url, format='JSON')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Mexico City, MX", response.data["location_name"])

    def test_get_weather_no_content_failed(self):
        url = "/weather"
        response = self.client.get(url, format='JSON')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_weather_wrong_data_failed(self):
        url = "/weather?city=Mexico&country=jp"
        response = self.client.get(url, format='JSON')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_weather_wrong_data_length_failed(self):
        url = "/weather?city=Mexico&country=jfp"
        response = self.client.get(url, format='JSON')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
