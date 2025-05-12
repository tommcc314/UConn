import unittest
from Lab2 import Polygon, Triangle, Rectangle


class TestLab2(unittest.TestCase):
    def test_init(self):

        a1 = Polygon(3);
        self.assertEqual(a1.whoamI(),"Triangle")
        self.assertEqual(a1.howmanysides(), 3)
        a2 = Polygon(4);
        self.assertEqual(a2.whoamI(),"Rectangle")
        self.assertEqual(a2.howmanysides(), 4)

    def test_area(self):
        a1 = Triangle(3,4,5)
        self.assertEqual(a1.area(), 6)
        a2 = Rectangle(3,4)
        self.assertEqual(a2.area(),12)
    def test_perimeter(self):
        a1 = Triangle(3, 4, 5)
        self.assertEqual(a1.perimeter(), 12)
        a2 = Rectangle(3, 4)
        self.assertEqual(a2.perimeter(), 14)


if (__name__ == '__main__'):
    unittest.main()
