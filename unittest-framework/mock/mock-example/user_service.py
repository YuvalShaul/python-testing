class Database:
    def get_user(self, user_id):
        # Imagine this actually connects to a database
        # and does complex queries
        return {"id": user_id, "name": "John Doe", "active": True}

    def update_login_count(self, user_id):
        # Imagine this updates a login counter in database
        pass

class UserService:
    def __init__(self, database):
        self.database = database

    def get_user_name(self, user_id):
        user = self.database.get_user(user_id)
        if user["active"]:
            self.database.update_login_count(user_id)
            return user["name"]
        return None