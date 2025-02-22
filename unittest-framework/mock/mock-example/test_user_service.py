import unittest
from unittest.mock import Mock
from user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        # Create a mock database
        self.mock_db = Mock()
        # Create our service using the mock database
        self.user_service = UserService(self.mock_db)

    def test_get_user_name_active_user(self):
        # Configure mock to return an active user
        self.mock_db.get_user.return_value = {
            "id": 1,
            "name": "John Doe",
            "active": True
        }

        # Call the method we're testing
        result = self.user_service.get_user_name(1)

        # Verify the result
        self.assertEqual(result, "John Doe")
        
        # Verify the database methods were called correctly
        self.mock_db.get_user.assert_called_once_with(1)
        self.mock_db.update_login_count.assert_called_once_with(1)

    def test_get_user_name_inactive_user(self):
        # Configure mock to return an inactive user
        self.mock_db.get_user.return_value = {
            "id": 1,
            "name": "John Doe",
            "active": False
        }

        # Call the method we're testing
        result = self.user_service.get_user_name(1)

        # Verify the result
        self.assertIsNone(result)
        
        # Verify get_user was called but update_login_count was not
        self.mock_db.get_user.assert_called_once_with(1)
        self.mock_db.update_login_count.assert_not_called()

if __name__ == '__main__':
    unittest.main()