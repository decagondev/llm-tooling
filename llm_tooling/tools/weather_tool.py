import requests
import yaml
from utils.logger import Logger
from tools.base_tool import BaseTool

class WeatherTool(BaseTool):
    def __init__(self):
        self.logger = Logger()
        with open('config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            self.api_key = config['weather']['api_key']
        self.base_url = "https://api.weatherapi.com/v1/current.json"

    def call(self, city):
        self.logger.log(f"Calling OpenWeatherMap API for city: {city}")
        params = {
            'q': city,
            'key': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                "weather": data["current"]['condition']['text'],
            }
            self.logger.log(f"Received weather data: {weather_info}")
            return f"The current weather in {city} is {weather_info["weather"]}"
        else:
            error_message = response.json().get('message', 'Unknown error occurred.')
            self.logger.log(f"Error fetching weather data: {error_message}")
            return {'error': error_message}
