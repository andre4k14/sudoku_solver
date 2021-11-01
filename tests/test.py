import unittest
import sudoku_solver.sudoku_solver as sus

test_1 = [[7, 9, 0, 2, 0, 0, 0, 6, 0], [2, 0, 0, 4, 0, 3, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 0, 0, 4, 0, 9], [0, 0, 2, 8, 0, 4, 7, 0, 0], [8, 0, 1, 0, 0, 0, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 6, 0, 8, 0, 0, 3], [0, 2, 0, 0, 0, 5, 0, 4, 8]]


class TestSudokuSolver(unittest.TestCase):

    def test_sudoku_array(self):
        t1 = sus.sudoku_array(test_1)
        self.assertEqual(t1.is_valid(), False)


if __name__ == '__main__':
    unittest.main()
