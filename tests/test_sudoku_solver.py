import pytest
from sudoku_solver.sudoku_solver import solve_sudoku as sus
from sudoku_solver.sudoku_solver import SudokuArray, sudoku_solver

test_1 = [[7, 9, 0, 2, 0, 0, 0, 6, 0], [2, 0, 0, 4, 0, 3, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 0, 0, 4, 0, 9], [0, 0, 2, 8, 0, 4, 7, 0, 0], [8, 0, 1, 0, 0, 0, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 6, 0, 8, 0, 0, 3], [0, 2, 0, 0, 0, 5, 0, 4, 8]]



def test_sudoku_array():
    t1 = sus(test_1)
    assert t1[1] == True
