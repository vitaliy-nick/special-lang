import unittest
from unittest.mock import patch
from Classes.api_repository import APIRepository  # Змініть шлях відповідно до структури проєкту


class TestAPIRepository(unittest.TestCase):
    @patch("requests.get")
    def test_get_users(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = [{"id": 1, "name": "John Doe"}]

        api_repo = APIRepository()
        result = api_repo.get_users()

        mock_get.assert_called_once_with(f"{APIRepository.BASE_URL}/users")
        self.assertEqual(result, [{"id": 1, "name": "John Doe"}])

    @patch("requests.get")
    def test_get_posts(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = [{"id": 1, "title": "Sample Post"}]

        api_repo = APIRepository()
        result = api_repo.get_posts()

        mock_get.assert_called_once_with(f"{APIRepository.BASE_URL}/posts")
        self.assertEqual(result, [{"id": 1, "title": "Sample Post"}])

    @patch("requests.post")
    def test_add_user(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"id": 101, "name": "Jane Doe", "email": "jane@example.com"}

        api_repo = APIRepository()
        result = api_repo.add_user(name="Jane Doe", email="jane@example.com")

        mock_post.assert_called_once_with(
            f"{APIRepository.BASE_URL}/users",
            json={"name": "Jane Doe", "email": "jane@example.com"}
        )
        self.assertEqual(result, {"id": 101, "name": "Jane Doe", "email": "jane@example.com"})

    @patch("requests.post")
    def test_add_post(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"id": 101, "title": "New Post", "body": "Post content", "userId": 1}

        api_repo = APIRepository()
        result = api_repo.add_post(title="New Post", body="Post content", user_id=1)

        mock_post.assert_called_once_with(
            f"{APIRepository.BASE_URL}/posts",
            json={"title": "New Post", "body": "Post content", "userId": 1}
        )
        self.assertEqual(result, {"id": 101, "title": "New Post", "body": "Post content", "userId": 1})
