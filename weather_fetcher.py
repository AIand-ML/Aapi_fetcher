import requests


class WeatherFetcher:

    city_coordinates = {
        "kathmandu": (27.7172, 85.3240),
        "pokhara": (28.2096, 83.9856),
        "butwal": (27.7000, 83.4500),
        "chitwan": (27.5291, 84.3542),
        "biratnagar": (26.4525, 87.2718)
    }

    def get_weather(self, city):

        city = city.lower()

        if city not in self.city_coordinates:
            raise ValueError("City not found")

        latitude, longitude = self.city_coordinates[city]

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current_weather=true"
        )

        response = requests.get(url)

        data = response.json()

        weather = data["current_weather"]

        return {
            "temperature": weather["temperature"],
            "windspeed": weather["windspeed"]
        }