import unittest
from unittest.mock import patch, Mock
from llm_tool_project.tools.weather_tool import WeatherTool

class TestWeatherTool(unittest.TestCase):
    def setUp(self):
        self.weather_tool = WeatherTool()

    @patch('llm_tooling.tools.weather_tool.requests.get')
    def test_call_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 20},
            'weather': [{'description': 'clear sky'}],
            'name': 'Test City'
        }
        mock_get.return_value = mock_response

        result = self.weather_tool.call('Test City')
        self.assertEqual(result['temperature'], 20)
        self.assertEqual(result['description'], 'clear sky')
        self.assertEqual(result['city'], 'Test City')

    @patch('llm_tool_project.tools.weather_tool.requests.get')
    def test_call_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {'message': 'city not found'}
        mock_get.return_value = mock_response

        result = self.weather_tool.call('Invalid City')
        self.assertEqual(result['error'], 'city not found')

if __name__ == '__main__':
    unittest.main()
