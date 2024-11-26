import unittest
from unittest.mock import MagicMock
from Classes.adder import Adder

class TestAdder(unittest.TestCase):
    def setUp(self):
        # Створюємо об'єкти, які будемо використовувати в тестах
        self.api_repository = MagicMock()
        self.local_users = []
        self.local_posts = []
        self.history_manager = MagicMock()
        self.adder = Adder(self.api_repository, self.local_users, self.local_posts, self.history_manager)

    def test_add_user(self):
        # Налаштовуємо мок API для повернення певних даних користувача
        self.api_repository.add_user.return_value = {"id": 1, "name": "Test User", "email": "test@example.com"}

        # Виконуємо метод
        self.adder.add_user("Test User", "test@example.com")

        # Перевіряємо, чи користувача додано в локальний список
        self.assertEqual(len(self.local_users), 1)
        self.assertEqual(self.local_users[0].name, "Test User")
        self.assertEqual(self.local_users[0].email, "test@example.com")

        # Перевіряємо, чи викликано метод для запису історії
        self.history_manager.log.assert_called_once_with("Add user", " User Test User (test@example.com) added.")

    def test_add_post(self):
        # Налаштовуємо мок API для повернення певних даних поста
        self.api_repository.add_post.return_value = {"id": 1, "title": "Test Post", "body": "Post body", "userId": 1}

        # Виконуємо метод
        self.adder.add_post("Test Post", "Post body", 1)

        # Перевіряємо, чи пост додано в локальний список
        self.assertEqual(len(self.local_posts), 1)
        self.assertEqual(self.local_posts[0].title, "Test Post")
        self.assertEqual(self.local_posts[0].body, "Post body")

        # Перевіряємо, чи викликано метод для запису історії
        self.history_manager.log.assert_called_once_with("Add post", "Post Test Post added.")
