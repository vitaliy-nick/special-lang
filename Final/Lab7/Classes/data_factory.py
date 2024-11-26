from Classes.user import User
from Classes.post import Post

class DataFactory:
    @staticmethod
    def create_user(data):
        return User(data["id"], data["name"], data["email"])

    @staticmethod
    def create_post(data):
        return Post(data["id"], data["title"], data["body"], data["userId"])
