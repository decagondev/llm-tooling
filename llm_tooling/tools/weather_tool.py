import requests
import yaml
from llm_tool_project.utils.logger import Logger
from llm_tool_project.tools.base_tool import BaseTool

class WeatherTool(BaseTool):
    def __init__(self):
        self.logger = Logger()
        with open('llm_tooling/config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            self.api_key = config['weather']['api_key']
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def call(self, city):
        self.logger.log(f"Calling OpenWeatherMap API for city: {city}")
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'city': data['name']
            }
            self.logger.log(f"Received weather data: {weather_info}")
            return weather_info
        else:
            error_message = response.json().get('message', 'Unknown error occurred.')
            self.logger.log(f"Error fetching weather data: {error_message}")
            return {'error': error_message}
