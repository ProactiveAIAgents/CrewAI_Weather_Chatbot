from typing import Dict

import requests

from config.config import FORECAST_API_BASE_URL, TOMORROW_API_KEY, WEATHER_API_BASE_URL


class WeatherTools:
    @staticmethod
    def get_current_weather(location: str) -> Dict:
        """Get current weather for a specific location"""
        params = {"location": location, "apikey": TOMORROW_API_KEY, "units": "metric"}

        response = requests.get(WEATHER_API_BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching weather data: {response.status_code}")

    @staticmethod
    def get_forecast(location: str) -> Dict:
        """Get 3-day forecast for a specific location"""
        params = {"location": location, "apikey": TOMORROW_API_KEY, "units": "metric"}

        response = requests.get(FORECAST_API_BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching forecast data: {response.status_code}")
