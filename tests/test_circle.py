import unittest
import math
import circle

class TestCircle(unittest.TestCase):

    def test_area_integer(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), 6.25 * math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter_integer(self):
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

 
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

    def test_area_small_float(self):
        self.assertAlmostEqual(
            circle.area(0.000001),
            math.pi * 0.000001 ** 2
        )

    def test_area_large_number(self):
        self.assertAlmostEqual(
            circle.area(1000000),
            math.pi * 1000000 ** 2
        )

    def test_area_negative_float(self):
        with self.assertRaises(ValueError):
            circle.area(-0.5)

    def test_area_none(self):
        with self.assertRaises(TypeError):
            circle.area(None)

    def test_perimeter_small_float(self):
        self.assertAlmostEqual(
            circle.perimeter(0.000001),
            2 * math.pi * 0.000001
        )

    def test_perimeter_large_number(self):
        self.assertAlmostEqual(
            circle.perimeter(1000000),
            2 * math.pi * 1000000
        )

    def test_perimeter_negative_float(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-0.5)

    def test_perimeter_bool(self):
        with self.assertRaises(TypeError):
            circle.perimeter(True)
    def test_area_non_finite_values(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    circle.area(value)

    def test_perimeter_non_finite_values(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    circle.perimeter(value)

    def test_area_unsupported_types(self):
        for value in ([1], (1,), 1 + 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    circle.area(value)

    def test_perimeter_unsupported_types(self):
        for value in ([1], (1,), 1 + 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    circle.perimeter(value)
                    
if __name__ == "__main__":
    unittest.main()
