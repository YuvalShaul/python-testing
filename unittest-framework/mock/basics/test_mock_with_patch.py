import unittest
from unittest.mock import patch
import requests  # You'll need this for the example

class UserService:
    def get_user_data(self):
        response = requests.get('https://api.example.com/users')   # No such a thing
        return response.json()

class TestUserService(unittest.TestCase):  # Notice the class inherits from unittest.TestCase
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        # Configure the mock
        mock_get.return_value.json.return_value = {'name': 'John Doe'}
        
        # Create instance and call method
        service = UserService()
        result = service.get_user_data()
        
        # Assertions
        self.assertEqual(result['name'], 'John Doe')
        mock_get.assert_called_once_with('https://api.example.com/users')

# Run with:
#   python -m unittest test_mock_with_patch