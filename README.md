# Globant-WeatherAPI

Prueba tecnica para Globant

# Prerequisitos

- [Docker](https://docs.docker.com/install/)
- [Docker-Compose](https://docs.docker.com/compose/)
- archivo .env

*Nota*
- sin el archivo .env el proyecto no correra
- Poner el archivo .env en la raiz del proyecto 



# Inicializar el proyecto

Correr el proyecto en local:

```bash
docker-compose up
```


## Ejemplo

```json
GET http://127.0.0.1:8000/weather?city=Mexico&country=mx
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "location_name": "Mexico City, MX",
    "temperature: ": "12°C",
    "wind :": "Clouds, 3.1 m/s",
    "cloudiness:": "few clouds",
    "pressure: ": "1031 hpa",
    "humidity: ": "66%",
    "sunrise:": "12:47:21",
    "sunset: ": "23:57:05",
    "geo_coordinates:": "[-99.13,19.43]",
    "requested_time:": "2020-11-20T05:46:57.376548"
}
```

## Ejemplo fallido
```json
GET http://127.0.0.1:8000/weather
HTTP 400 Bad Request
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "status": "required fields not found"
}
```

