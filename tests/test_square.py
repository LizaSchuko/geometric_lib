
import unittest
import math
import square
class TestSquare(unittest.TestCase):

    def test_area_integer(self):
        self.assertEqual(square.area(5), 25)

    def test_area_float(self):
        self.assertEqual(square.area(2.5), 6.25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)


    def test_perimeter_integer(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_float(self):
        self.assertEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

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

    def test_area_small_float(self):
        self.assertEqual(square.area(0.000001), 1e-12)

    def test_area_large_number(self):
        self.assertEqual(square.area(1000000), 1000000000000)

    def test_area_negative_float(self):
        with self.assertRaises(ValueError):
            square.area(-0.5)

    def test_area_none(self):
        with self.assertRaises(TypeError):
            square.area(None)

    def test_perimeter_small_float(self):
        self.assertEqual(square.perimeter(0.000001), 4e-06)

    def test_perimeter_large_number(self):
        self.assertEqual(square.perimeter(1000000), 4000000)

    def test_perimeter_negative_float(self):
        with self.assertRaises(ValueError):
            square.perimeter(-0.5)

    def test_perimeter_bool(self):
        with self.assertRaises(TypeError):
            square.perimeter(True)
    def test_area_non_finite_values(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    square.area(value)

    def test_perimeter_non_finite_values(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    square.perimeter(value)

    def test_area_unsupported_types(self):
        for value in ([1], (1,), 1 + 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    square.area(value)

    def test_perimeter_unsupported_types(self):
        for value in ([1], (1,), 1 + 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    square.perimeter(value)
if __name__ == "__main__":
    unittest.main()
