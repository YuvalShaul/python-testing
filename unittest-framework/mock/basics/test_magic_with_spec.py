# First, let's define a class with specific methods
class UserAPI:
    def get_user(self, user_id):
        # Imagine real implementation here
        return {"id": user_id, "name": "Real User"}
    
    def save_user(self, user_data):
        # Imagine real implementation here
        pass

# Now let's demonstrate spec with MagicMock
from unittest.mock import MagicMock

# Create MagicMock with spec
mock_api = MagicMock(spec=UserAPI)

# These work because they're in the spec
mock_api.get_user(1)
mock_api.save_user({"name": "Test"})

# This raises AttributeError because delete_user isn't in UserAPI
try:
    mock_api.delete_user(1)
except AttributeError as e:
    print("Error:", e)

# You can still set return values for specified methods
mock_api.get_user.return_value = {"id": 1, "name": "Mocked User"}
result = mock_api.get_user(1)
print(result)  # {"id": 1, "name": "Mocked User"}

# Verify calls work the same way
mock_api.get_user.assert_called_with(1)