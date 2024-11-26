import unittest
from unittest.mock import patch
from classes import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Тест перевіряє правильне введення чисел і оператора
    @patch('builtins.input', side_effect=['10', '+', '1'])
    def test_get_input_valid(self, mock_input):
        num1, operator, num2 = self.calc.get_input()
        self.assertEqual(num1, 10.0)
        self.assertEqual(operator, '+')
        self.assertEqual(num2, 1.0)

    # Тест перевіряє використання пам'яті та оператора квадратного кореня
    @patch('builtins.input', side_effect=['m', '√'])
    def test_get_input_memory_sqrt(self, mock_input):
        self.calc.memory.set_memory(16.0)
        num1, operator, num2 = self.calc.get_input()
        self.assertEqual(num1, 16.0)
        self.assertEqual(operator, '√')
        self.assertIsNone(num2)

    # Тест перевіряє обробку неправильного оператора та повторне запитання оператора
    @patch('builtins.input', side_effect=['$', '+'])
    def test_get_operator_invalid_then_valid(self, mock_input):
        operator = self.calc.get_operator()
        self.assertEqual(operator, '+')

    # Тест перевіряє правильність розпізнавання коректних операторів
    def test_check_operator_valid(self):
        self.assertTrue(self.calc.check_operator('+'))
        self.assertTrue(self.calc.check_operator('-'))
        self.assertTrue(self.calc.check_operator('*'))
        self.assertTrue(self.calc.check_operator('/'))
        self.assertTrue(self.calc.check_operator('^'))
        self.assertTrue(self.calc.check_operator('√'))
        self.assertTrue(self.calc.check_operator('%'))

    # Тест перевіряє розпізнавання некоректних операторів
    def test_check_operator_invalid(self):
        self.assertFalse(self.calc.check_operator('&'))
        self.assertFalse(self.calc.check_operator('!'))
        self.assertFalse(self.calc.check_operator('incorrect'))
        self.assertFalse(self.calc.check_operator('1'))

    # Тест перевіряє встановлення та отримання значення з пам'яті
    def test_memory_set_get(self):
        self.calc.memory.set_memory(10)
        self.assertEqual(self.calc.memory.get_memory(), 10)

    # Тест перевіряє очищення пам'яті
    def test_memory_clear(self):
        self.calc.memory.set_memory(10)
        self.calc.memory.clear_memory()
        self.assertEqual(self.calc.memory.get_memory(), 0)

    # Тест перевіряє додавання записів в історію та перевірку наявності запису
    def test_history_add_and_show(self):
        self.calc.history.add_to_history("2 + 2", 4)
        self.assertIn("2 + 2 = 4", self.calc.history._History__history)

    # Тест перевіряє встановлення кількості знаків після коми
    def test_set_decimal_places(self):
        with patch('builtins.input', side_effect=['2']):
            self.calc.settings.set_decimal_places()
            self.assertEqual(self.calc.settings.get_decimal_places(), 2)

    # Тест перевіряє обробку неправильного введення для кількості знаків після коми
    def test_set_decimal_places_invalid(self):
        with patch('builtins.input', side_effect=['-1']):
            with self.assertRaises(ValueError):
                self.calc.settings.set_decimal_places()

    # Тести для базових операцій: додавання, віднімання, множення, ділення
    def test_addition(self):
        self.assertEqual(self.calc.perform_operators(2, '+', 2), 4)
        self.assertEqual(self.calc.perform_operators(-2, '+', -2), -4)
        self.assertEqual(self.calc.perform_operators(-2, '+', 2), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.perform_operators(2, '-', 2), 0)
        self.assertEqual(self.calc.perform_operators(-2, '-', -2), 0)
        self.assertEqual(self.calc.perform_operators(2, '-', 4), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.perform_operators(2, '*', 2), 4)
        self.assertEqual(self.calc.perform_operators(2, '*', 0), 0)
        self.assertEqual(self.calc.perform_operators(-2, '*', 2), -4)

    def test_division(self):
        self.assertEqual(self.calc.perform_operators(4, '/', 2), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calc.perform_operators(2, '/', 0)

    # Тест для операції квадратного кореня
    def test_square_root(self):
        self.assertEqual(self.calc.perform_operators(4, '√', None), 2)
        with self.assertRaises(ValueError):
            self.calc.perform_operators(-4, '√', None)

    # Тест для операції остачі від ділення (modulo)
    def test_modulo(self):
        self.assertEqual(self.calc.perform_operators(5, '%', 3), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calc.perform_operators(1, '%', 0)

    # Тести для операції піднесення до степеня (exponentiation)
    def test_exponentiation(self):
        self.assertEqual(self.calc.perform_operators(2, '^', 2), 4)
        self.assertEqual(self.calc.perform_operators(2, '^', 0), 1)
        self.assertEqual(self.calc.perform_operators(-2, '^', 2), -4)
        self.assertEqual(self.calc.perform_operators(2, '^', -1), 0.5)

if __name__ == '__main__':
    unittest.main()
