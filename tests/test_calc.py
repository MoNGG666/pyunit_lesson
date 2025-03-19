import math
import unittest
from parameterized import parameterized
from app.main import Calculator
from app.error import InvalidInputException

class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    # Тест на корректные входные данные
    @parameterized.expand([
        ("positive integers", 8, 2, 3.0),
        ("base 10", 100, 10, 2.0),
        ("fractional base", 4, 0.5, -2.0),
        ("natural log base e", math.e, math.e, 1.0),
        ("a is 1", 1, 5, 0.0),  # Теперь должен проходить
    ])
    def test_log_valid_input(self, name, a, base, expected_result):
        actual_result = self.calc.log(a, base)
        self.assertAlmostEqual(actual_result, expected_result)

    # Тест на неверные типы данных
    @parameterized.expand([
        ("string a", 'a', 2, TypeError),
        ("string base", 2, 'b', TypeError),
        ("None a", None, 10, TypeError),
        ("None base", 5, None, TypeError),
        ("list as a", [1], 2, TypeError),
    ])
    def test_log_invalid_types(self, name, a, base, expected_exception):
        with self.assertRaises(expected_exception):
            self.calc.log(a, base)

    # Тест на InvalidInputException
    @parameterized.expand([
        ("a is zero", 0, 2, InvalidInputException),
        ("a negative", -5, 10, InvalidInputException),
        ("base is zero", 5, 0, InvalidInputException),
        ("base negative", 10, -3, InvalidInputException),
        ("base is 1", 2, 1, InvalidInputException),  # Теперь должен проходить
    ])
    def test_log_invalid_input_exception(self, name, a, base, expected_exception):
        with self.assertRaises(expected_exception):
            self.calc.log(a, base)


if __name__ == "__main__":
    unittest.main()