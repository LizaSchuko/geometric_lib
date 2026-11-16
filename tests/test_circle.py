import unittest
import math

import circle


class TestCircle(unittest.TestCase):

    # Тесты площади круга
    def test_area_integer(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), 6.25 * math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    # Тесты длины окружности
    def test_perimeter_integer(self):
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    # Тесты обработки ошибок
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-2)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-2)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("2")

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("2")

    def test_area_bool(self):
        with self.assertRaises(TypeError):
            circle.area(True)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)


if __name__ == "__main__":
    unittest.main()
