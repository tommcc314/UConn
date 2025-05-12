from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
            self.assertEqual(puzzle([2,1,2,5,0]), True)
            self.assertEqual(puzzle([2,3,4,0,0]), True)
            self.assertEqual(puzzle([4,0,2,3,0]), True)
            self.assertEqual(puzzle([3,2,5,1,0]), True)

        def testCounterClockwise(self):
            self.assertEqual(puzzle([3,2,3,0,0]), True)
            self.assertEqual(puzzle([1,5,3,2,0]), True)
            self.assertEqual(puzzle([2,1,0,4,0]), True)
            self.assertEqual(puzzle([3,2,1,5,0]), True)

        def testMixed(self):
            self.assertEqual(puzzle([2,1,3,2,0]), True)
            self.assertEqual(puzzle([3,1,2,3,0]), True)
            self.assertEqual(puzzle([2,1,4,1,0]), True)
            self.assertEqual(puzzle([3,3,1,2,0]), True)
        
        def testUnsolveable(self):
            self.assertEqual(puzzle([5,3,2,2,0]), False) #trivial
            self.assertEqual(puzzle([3,1,1,2,0]), False)
            self.assertEqual(puzzle([2,0,1,3,0]), False)
            self.assertEqual(puzzle([2,4,1,2,0]), False)

if __name__ == "__main__":
        unittest.main()