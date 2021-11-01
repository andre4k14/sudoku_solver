import sys
import signal
from sudoku_solver.sudoku_solver import solve_sudoku


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    test_1 = [[7, 9, 0, 2, 0, 0, 0, 6, 0], [2, 0, 0, 4, 0, 3, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 7, 0, 0, 0, 0, 4, 0, 9], [0, 0, 2, 8, 0, 4, 7, 0, 0], [8, 0, 1, 0, 0, 0, 0, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 6, 0, 8, 0, 0, 3], [0, 2, 0, 0, 0, 5, 0, 4, 8]]
    print(solve_sudoku())


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
