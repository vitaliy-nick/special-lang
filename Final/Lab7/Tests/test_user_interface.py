import unittest
from unittest.mock import patch, MagicMock
from Classes.console_app import ConsoleApp
from UI.user_interface import main


class TestConsoleApp(unittest.TestCase):

    def setUp(self):
        pass

    @patch.object(ConsoleApp, 'show_users')
    @patch('builtins.input', side_effect=["1", "10"])
    def test_show_users_option(self, mock_input, mock_show_users):
        # Перевірка, чи викликається show_users при виборі опції 1
        main()
        mock_show_users.assert_called_once()

    @patch.object(ConsoleApp, 'show_posts')
    @patch('builtins.input', side_effect=["2", "10"])
    def test_show_posts_option(self, mock_input, mock_show_posts):
        main()
        mock_show_posts.assert_called_once()

    @patch.object(ConsoleApp, 'add_user')
    @patch('builtins.input', side_effect=["3", "10"])
    def test_add_user_option(self, mock_input, mock_add_user):
        main()
        mock_add_user.assert_called_once()

    @patch.object(ConsoleApp, 'add_post')
    @patch('builtins.input', side_effect=["4", "10"])
    def test_add_post_option(self, mock_input, mock_add_post):
        main()
        mock_add_post.assert_called_once()

    @patch.object(ConsoleApp, 'delete_user')
    @patch('builtins.input', side_effect=["5", "10"])
    def test_delete_user_option(self, mock_input, mock_delete_user):
        main()
        mock_delete_user.assert_called_once()

    @patch.object(ConsoleApp, 'delete_post')
    @patch('builtins.input', side_effect=["6", "10"])
    def test_delete_post_option(self, mock_input, mock_delete_post):
        main()
        mock_delete_post.assert_called_once()

    @patch.object(ConsoleApp, 'save_users')
    @patch('builtins.input', side_effect=["7", "10"])
    def test_save_users_option(self, mock_input, mock_save_users):
        main()
        mock_save_users.assert_called_once()

    @patch.object(ConsoleApp, 'save_posts')
    @patch('builtins.input', side_effect=["8", "10"])
    def test_save_posts_option(self, mock_input, mock_save_posts):
        main()
        mock_save_posts.assert_called_once()

    @patch.object(ConsoleApp, 'show_history')
    @patch('builtins.input', side_effect=["9", "10"])
    def test_show_history_option(self, mock_input, mock_show_history):
        main()
        mock_show_history.assert_called_once()

    @patch('builtins.input', side_effect=["11", "10"])
    def test_invalid_option(self, mock_input):
        # Тест для некоректного вибору опції
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Error: Incorrect option! Please, try adain!")

