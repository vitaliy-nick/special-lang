import unittest
from unittest.mock import patch, mock_open, call
from Classes.file_manager import DataSaver  # Шлях змінити відповідно до вашої структури проєкту
import json
import csv


class TestDataSaver(unittest.TestCase):
    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_json(self, mock_file_open, mock_makedirs):
        data = {"key": "value"}
        filename = "test.json"

        DataSaver.save_to_json(data, filename)

        mock_makedirs.assert_called_once_with("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Data", exist_ok=True)
        mock_file_open.assert_called_once_with("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Data/test.json", "w")
        handle = mock_file_open()
        handle.write.assert_called_once_with(json.dumps(data, indent=4))

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_csv(self, mock_file_open, mock_makedirs):
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        filename = "test.csv"

        DataSaver.save_to_csv(data, filename)

        mock_makedirs.assert_called_once_with("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Data", exist_ok=True)
        mock_file_open.assert_called_once_with("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Data/test.csv", "w", newline='')
        handle = mock_file_open()
        writer = csv.DictWriter(handle, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_txt(self, mock_file_open, mock_makedirs):
        data = ["Line 1", "Line 2", "Line 3"]
        filename = "test.txt"

        DataSaver.save_to_txt(data, filename)

        mock_makedirs.assert_called_once_with("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Data", exist_ok=True)
        mock_file_open.assert_called_once_with("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Data/test.txt", "w")
        handle = mock_file_open()
        expected_calls = [call("Line 1\n"), call("Line 2\n"), call("Line 3\n")]
        handle.write.assert_has_calls(expected_calls, any_order=False)

    @patch("builtins.input", side_effect=["1", "test_file"])
    @patch("Classes.data_saver.DataSaver.save_to_json")  # Замінити на правильний шлях до DataSaver
    def test_select_save_format_json(self, mock_save_to_json, mock_input):
        data = {"key": "value"}

        DataSaver.select_save_format(data, "json")

        mock_save_to_json.assert_called_once_with(data, "test_file.json")

    @patch("builtins.input", side_effect=["2", "test_file"])
    @patch("Classes.data_saver.DataSaver.save_to_csv")  # Замінити на правильний шлях до DataSaver
    def test_select_save_format_csv(self, mock_save_to_csv, mock_input):
        data = [{"name": "Alice"}, {"name": "Bob"}]

        DataSaver.select_save_format(data, "csv")

        mock_save_to_csv.assert_called_once_with(data, "test_file.csv")

    @patch("builtins.input", side_effect=["3", "test_file"])
    @patch("Classes.data_saver.DataSaver.save_to_txt")  # Замінити на правильний шлях до DataSaver
    def test_select_save_format_txt(self, mock_save_to_txt, mock_input):
        data = ["Line 1", "Line 2"]

        DataSaver.select_save_format(data, "txt")

        mock_save_to_txt.assert_called_once_with(data, "test_file.txt")

    @patch("builtins.input", side_effect=["4", "test_file"])
    @patch("builtins.print")
    def test_select_save_format_invalid_option(self, mock_print, mock_input):
        data = ["Line 1", "Line 2"]

        with self.assertRaises(RecursionError):
            DataSaver.select_save_format(data, "txt")

        mock_print.assert_called_with("Error: Incorrect option! Please, try again!")
