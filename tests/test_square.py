
import unittest

import square


class TestSquare(unittest.TestCase):

    # Тесты площади квадрата
    def test_area_integer(self):
        self.assertEqual(square.area(5), 25)

    def test_area_float(self):
        self.assertEqual(square.area(2.5), 6.25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    # Тесты периметра квадрата
    def test_perimeter_integer(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_float(self):
        self.assertEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    # Тесты обработки ошибок
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            square.area("5")

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("5")

    def test_area_bool(self):
        with self.assertRaises(TypeError):
            square.area(True)

    def test_perimeter_none(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)


if __name__ == "__main__":
    unittest.main()
