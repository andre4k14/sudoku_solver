import sys
import signal
from sudoku_solver.sudokusolver import SudokuArray, SudokuSolver
from sudoku_solver import solve_sudoku


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    test_1 = [[7, 9, 0, 2, 0, 0, 0, 6, 0],
              [2, 0, 0, 4, 0, 3, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 7, 0, 0, 0, 0, 4, 0, 9],
              [0, 0, 2, 8, 0, 4, 7, 0, 0],
              [8, 0, 1, 0, 0, 0, 0, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [5, 0, 0, 6, 0, 8, 0, 0, 3],
              [0, 2, 0, 0, 0, 5, 0, 4, 8]]

    test_2 = [[5, 0, 0, 4, 0, 0, 0, 0, 9],
              [9, 0, 0, 0, 0, 0, 4, 0, 7],
              [0, 0, 0, 0, 0, 0, 0, 5, 0],
              [6, 0, 2, 0, 4, 9, 0, 0, 0],
              [0, 7, 0, 0, 6, 3, 0, 0, 0],
              [0, 3, 0, 7, 0, 0, 6, 0, 8],
              [2, 0, 0, 1, 3, 6, 0, 7, 5],
              [0, 0, 5, 9, 0, 8, 2, 0, 0],
              [0, 8, 3, 0, 0, 4, 9, 1, 0]]

    test_3 = [[1, 0, 5, 0, 0, 0, 4, 9, 2],
              [0, 0, 2, 1, 4, 5, 0, 8, 3],
              [0, 3, 6, 2, 0, 9, 0, 0, 5],
              [8, 0, 0, 0, 6, 0, 2, 0, 9],
              [7, 0, 0, 8, 1, 0, 3, 4, 6],
              [0, 6, 3, 0, 9, 4, 0, 0, 1],
              [0, 1, 4, 0, 0, 8, 5, 0, 7],
              [0, 9, 0, 0, 3, 0, 0, 0, 0],
              [3, 0, 0, 0, 5, 0, 9, 6, 8]]

    test_4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],  # empty
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    test_5 = [[1, 0, 0, 0, 0, 0, 0, 0, 2],  # unsolvable
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 4, 0, 0, 0, 3, 0, 0],
              [0, 0, 0, 1, 0, 2, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 3, 0, 4, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [3, 0, 0, 0, 0, 0, 0, 0, 4]]

    solve_sudoku(test_1, 2)

    sudoku = SudokuArray(test_2)
    sudoku = SudokuArray(test_3)
    sudoku = SudokuArray(test_4)
    sudoku = SudokuArray(test_5)
    sudoku_s = SudokuSolver(sudoku)
    sudoku_s.solve(10)
    sudoku_solved = sudoku_s.solved_sudoku_array
    print(sudoku_solved.create_representation_sudoku())
    sudoku_solved.print_sudoku()
    print(sudoku_solved.create_representation_sudoku())


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
