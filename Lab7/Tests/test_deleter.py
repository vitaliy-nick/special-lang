import unittest
from unittest.mock import MagicMock
from Classes.deleter import Deleter
from Classes.user import User
from Classes.post import Post

class TestDeleter(unittest.TestCase):
    def setUp(self):
        # Створюємо тестові дані
        self.local_users = [User(1, "User1", "user1@example.com")]
        self.local_posts = [Post(1, "Title1", "Body1", 1)]
        self.history_manager = MagicMock()
        self.deleter = Deleter(self.local_users, self.local_posts, self.history_manager)

    def test_delete_user_found(self):
        # Виконуємо видалення користувача
        self.deleter.delete_user(1)

        # Перевіряємо, чи користувача видалено
        self.assertEqual(len(self.local_users), 0)

        # Перевіряємо, чи викликано метод для запису історії
        self.history_manager.log.assert_called_once_with("Delete user", "User with ID 1 was deleted.")

    def test_delete_user_not_found(self):
        # Виконуємо видалення користувача, якого немає
        self.deleter.delete_user(2)

        # Перевіряємо, чи кількість користувачів не змінилася
        self.assertEqual(len(self.local_users), 1)

        # Перевіряємо, чи не викликано метод для запису історії
        self.history_manager.log.assert_not_called()

    def test_delete_post_found(self):
        # Виконуємо видалення поста
        self.deleter.delete_post(1)

        # Перевіряємо, чи пост видалено
        self.assertEqual(len(self.local_posts), 0)

        # Перевіряємо, чи викликано метод для запису історії
        self.history_manager.log.assert_called_once_with("Delete post", "Post with ID 1 was deleted.")

    def test_delete_post_not_found(self):
        # Виконуємо видалення поста, якого немає
        self.deleter.delete_post(2)

        # Перевіряємо, чи кількість постів не змінилася
        self.assertEqual(len(self.local_posts), 1)

        # Перевіряємо, чи не викликано метод для запису історії
        self.history_manager.log.assert_not_called()

