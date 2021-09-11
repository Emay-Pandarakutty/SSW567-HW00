import unittest
from main import classify_triangle

class MyTestCase(unittest.TestCase):
    def test_triangle_normal(self):
        self.assertEqual(classify_triangle(9, 12, 15), 'right', '(9, 12, 15) is a Right triangle')
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene', '4, 5, 6) is a scalene triangle')
        self.assertEqual(classify_triangle(7, 7, 8), 'isosceles', '(7, 7, 8) is a isosceles triangle')
        self.assertEqual(classify_triangle(7, 7, 7), 'equilateral', '(7, 7, 7) is a equilateral triangle')
        self.assertEqual(classify_triangle(7, 8, 16), 'Not a triangle', '(7, 8, 16) is Not a triangle')

    def test_triangle_robust(self):
        #checking float
        self.assertEqual(classify_triangle(1.23, 1.23, 1.23), 'equilateral', '(1.23, 1.23, 1.23) is a equilateral')
        #checking string
        self.assertEqual(classify_triangle("s", "s", "s"), 'equilateral', '(1.23, 1.23, 1.23) is a equilateral')
        #checking negative value
        self.assertEqual(classify_triangle(7, 7, -1), 'Not a triangle', '(7, 7, -1) is Not a triangle')

if __name__ == '__main__':
    unittest.main()
