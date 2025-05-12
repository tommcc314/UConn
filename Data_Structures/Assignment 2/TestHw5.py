from hw2a import solveable, valid_moves
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                # TODO: Fill in the data to test valid_moves on the board above
                k_idx = (7,0)
                expected_valid_moves = {(5,1),(6,2)}
                self.assertEqual(valid_moves(k_idx),expected_valid_moves)

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (0,0)
                expected_valid_moves = {(2,1),(1,2)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (0,7)
                expected_valid_moves = {(1,5),(2,6)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k
                k_idx = (7,7)
                expected_valid_moves = {(6,5),(5,6)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                k_idx = (3,3)
                expected_valid_moves = {(1,2),(1,4),(2,1),(2,5),(4,1),(4,5),(5,2),(5,4)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                # - - - - - p - -
                # - - p - - - - -
                # - - - - - k - -
                # - - - - p - - -
                # - - - - - - - -
                # - p - - p - - -
                # - - - - - - - -
                # - - - - - - - -
                self.assertEqual(solveable([(0,5),(1,2),(3,4),(5,1),(5,4)],(2,5)), False) #trivial

                #harder unsolveables:

                # - - - - - - - -
                # - - - - - - - -
                # - - - - p - - -
                # - - p - - - - -
                # - - - - p - - -
                # - p - - - - p -
                # - - - k - - - -
                # - - - - - p - -
                self.assertEqual(solveable([(2,4),(3,2),(4,4),(5,1),(5,6),(7,5)],(6,3)), False)

                # - - - - - - - -
                # - - - - - p - -
                # - - - p - - p -
                # - - - - p - - -
                # - - p p - - - k
                # - - - - - p - -
                # - - - - - - - -
                # - - - - - - - -
                self.assertEqual(solveable([(1,5),(2,3),(2,6),(3,4),(4,3),(4,2),(5,5)],(4,7)), False)

        def testSolveableSimple(self):
                # k - - - - - - -
                # - - p - - - - -
                # - - - - p - - -
                # - - - - - - - -
                # - p - - - p - -
                # - - - p - - - -
                # - - - - - - - -
                # - - - - - - - -
                self.assertEqual(solveable([(1,2),(2,4),(4,5),(4,1),(5,3)],(0,0)), True)
                # - - - - - - - -
                # - p - - - - - -
                # - - - p - - - -
                # - - - - p - - -
                # - - p - - - - -
                # - - - - - p - -
                # - - - - - - k -
                # - - - - p - - -
                self.assertEqual(solveable([(1,1),(2,3),(3,4),(4,2),(5,5),(7,4)],(6,6)),True)

        def testSolveableHard(self):
                # - - - - - - - -
                # - - p - - - - -
                # - - - - p - - -
                # - p p - - - - -
                # - - - k - - - -
                # - - p - p p - -
                # - - - - - - p -
                # - - - p p - - -
                self.assertEqual(solveable([(1,2),(2,4),(3,1),(3,2),(5,2),(5,4),(5,5),(6,6),(7,3),(7,4)],(4,3)), True)

                # - - - p - - - -
                # - - - - p k - p
                # - - p p p p - -
                # - - - - - p p -
                # - - - - - - - -
                # - - - - - - - -
                # - - - - - - - -
                # - - - - - - - -
                self.assertEqual(solveable([(0,3),(1,4),(1,7),(2,2),(2,3),(2,4),(2,5),(3,5),(3,6)],(1,5)), True)
if __name__ == "__main__":
        unittest.main()
