import unittest
from unittest.mock import patch, MagicMock
from Classes.console_app import ConsoleApp

class TestConsoleApp(unittest.TestCase):

    def setUp(self):
        # Ініціалізуємо екземпляр ConsoleApp перед кожним тестом
        self.app = ConsoleApp()

        # Мокаємо залежні об'єкти
        self.app.api_repository = MagicMock()
        self.app.history_manager = MagicMock()
        self.app.deleter = MagicMock()
        self.app.adder = MagicMock()
        self.app.local_users = []
        self.app.local_posts = []

        # Мокаємо зовнішні методи, щоб не виконували реальні HTTP-запити та інші дії
        self.app.api_repository.get_users.return_value = [{"id": 1, "name": "John Doe", "email": "john@example.com"}]
        self.app.api_repository.get_posts.return_value = [
            {"id": 1, "title": "Post 1", "body": "Content of post 1", "userId": 1}]

    @patch('builtins.print')
    def test_show_users(self, mock_print):
        # Тестуємо метод show_users
        self.app.show_users()
        # Перевіряємо, що викликано правильно виведення на екран через print
        mock_print.assert_called_with(
            '+------+--------------------------+---------------------------+\n|   ID | Name                     | Email                     |\n+======+==========================+===========================+\n|    1 | John Doe            | john@example.com         |\n+------+--------------------------+---------------------------+'
        )
        self.app.history_manager.log.assert_called_with("Show users", "All users.")

    @patch('builtins.print')
    def test_show_posts(self, mock_print):
        # Тестуємо метод show_posts
        self.app.show_posts()
        # Перевіряємо, що викликано правильно виведення на екран через print
        mock_print.assert_called_with(
            '+------+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+\n|   ID | Title                                                                           | Text                                                                             |   User ID |\n+======+=================================================================================+==================================================================================+===========+\n|    1 | Post 1      | Content of post 1                                                                 |         1 |'
        )
        self.app.history_manager.log.assert_called_with("Show posts", "All posts.")

    @patch('builtins.input', side_effect=["Alice", "alice@example.com"])
    def test_add_user(self, mock_input):
        # Тестуємо метод add_user
        self.app.add_user()
        self.app.adder.add_user.assert_called_with("Alice", "alice@example.com")

    @patch('builtins.input', side_effect=["New Post", "This is a test post", "1"])
    def test_add_post(self, mock_input):
        # Тестуємо метод add_post
        self.app.add_post()
        self.app.adder.add_post.assert_called_with("New Post", "This is a test post", 1)

    @patch('builtins.input', side_effect=["1"])
    def test_delete_user(self, mock_input):
        # Тестуємо метод delete_user
        self.app.delete_user()
        self.app.deleter.delete_user.assert_called_with(1)

    @patch('builtins.input', side_effect=["1"])
    def test_delete_post(self, mock_input):
        # Тестуємо метод delete_post
        self.app.delete_post()
        self.app.deleter.delete_post.assert_called_with(1)

    @patch('Classes.data_factory.DataSaver.select_save_format')
    def test_save_users(self, mock_save_format):
        # Тестуємо метод save_users
        self.app.save_users()
        self.app.api_repository.get_users.assert_called_once()
        mock_save_format.assert_called_once()

    @patch('Classes.data_factory.DataSaver.select_save_format')
    def test_save_posts(self, mock_save_format):
        # Тестуємо метод save_posts
        self.app.save_posts()
        self.app.api_repository.get_posts.assert_called_once()
        mock_save_format.assert_called_once()

    @patch('builtins.print')
    def test_show_history(self, mock_print):
        # Тестуємо метод show_history
        self.app.show_history()
        self.app.history_manager.show_history.assert_called_once()

