import unittest, random
from lab6 import OrderedList as OL
class TestLab6(unittest.TestCase):
    def testbs(self):
        L1 = OL([2,5,6,8,9,11,15,17])
        self.assertEqual(L1.__contains__(8), True)
        self.assertEqual(L1.__contains__(7), False)

if __name__ == "__main__":
    unittest.main()