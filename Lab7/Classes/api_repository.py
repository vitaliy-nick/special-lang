import requests

class APIRepository:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self):
        response = requests.get(f"{self.BASE_URL}/users")
        response.raise_for_status()
        return response.json()

    def get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()
        return response.json()

    def add_user(self, name, email):
        payload = {"name": name, "email": email}
        response = requests.post(f"{self.BASE_URL}/users", json=payload)
        response.raise_for_status()
        return response.json()

    def add_post(self, title, body, user_id):
        payload = {"title": title, "body": body, "userId": user_id}
        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        response.raise_for_status()
        return response.json()
