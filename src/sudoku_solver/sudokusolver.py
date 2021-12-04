from typing import Optional

import copy
from timeit import default_timer as timer

"""
s_array is

a 2d list (9x9) with integers between 0-9

0 if the spot is empty
1-9 for the number in the spot
"""
s_array = list[list[int]]


class SudokuArray:
    def __init__(self, array: s_array):
        """

        :param array: s_array
        """
        self.array: s_array = array

    def get_row(self, row: int) -> list[int]:
        """
        This method returns a list with all numbers in a row

        :param row: int 0-8
        :return: list with all ints in the row
        """
        return self.array[row]

    def get_column(self, column: int) -> list[int]:
        """
        This method returns a list with all numbers in a column

        :param column: int 0-8
        :return: list with all ints in the column
               """
        return [row[column] for row in self.array]

    def get_square(self, square: int) -> list[int]:
        """
         This method returns a list with all numbers in a square

         0|1|2
         -----
         3|4|5
         -----
         6|7|8

        :param square:  int 0-8
        :return: list with all ints in the square
        """

        a = -1
        b = square
        while b > -1:
            b -= 3
            a += 1

        a *= 3
        b = (square - a) * 3

        square_array = []

        for row in range(a, a + 3):
            for num in range(b, b + 3):
                square_array.append(self.array[row][num])
        return square_array

    def get_next_num_pos(self) -> list[int]:
        """
        This method returns the next position that's empty (value = 0), going form the top to bottom.
        If all positions full [-1,-1] gets returned. [row,column]
        :return: a list with the position of the next empty value, if none then [-1,-1]
        """

        for i, row in enumerate(self.array):
            for i2, num in enumerate(row):
                if num == 0:
                    return [i, i2]
        return [-1, -1]

    def is_valid_num(self, row: int, column: int, number: int) -> bool:
        """
        This method checks if having some number the some position is valid.
        :param row:  int 0-8
        :param column:  int 0-8
        :param number:  int 1-9
        :return: True if position is valid else False.
        """
        self.array[row][column] = number

        num_row = self.get_row(row)
        num_column = self.get_column(column)
        num_square = self.get_square((3 * (row // 3)) + (column // 3))

        if num_row.count(number) == 1 and num_column.count(number) == 1 and num_square.count(number) == 1:
            self.array[row][column] = 0
            return True
        self.array[row][column] = 0
        return False

    def is_valid(self) -> bool:
        """
        Checks if the whole sudoku puzzle is valid
        :return: True if valid else False.
        """
        valid = []
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i, row in enumerate(self.array):
            for i2, num in enumerate(row):
                n_row = self.get_row(i)
                n_column = self.get_column(i2)
                n_square = self.get_square((3 * (i // 3)) + (i2 // 3))

                all_n = n_row + n_column + n_square

                valid.append(all([True if all_n.count(_) == 3 else False for _ in numbers]))

        return all(valid)

    def create_representation_sudoku(self) -> str:
        """
        Prints the sudoku puzzle.
        :return: None
        """
        msg = ""

        for index, row in enumerate(self.array):
            if index % 3 == 0 and index != 0:
                msg += f"{('-' * 21)}\n"
            row_ = ""
            for i, num in enumerate(row):
                if i % 3 == 0 and i != 0:
                    row_ += "| "
                if num == 0:
                    str_num = " "
                else:
                    str_num = str(num)

                if i != 8:
                    str_num += " "

                row_ += str_num

            if index != 8:
                msg += f"{row_}\n"
            else:
                msg += f"{row_}"

        return msg

    def print_sudoku(self) -> None:
        print(f"\n{self.create_representation_sudoku()}\n", end="")


class SudokuSolver:
    def __init__(self, c_sudoku_array: SudokuArray):
        """

        :param c_sudoku_array: a sudoku_array object
        """
        self.sudoku_array: SudokuArray = c_sudoku_array
        self.possible_nums: list[list[list[int]]] = self.possible_nums_gen()

        self.solved_sudoku_array: Optional[SudokuArray] = None

        self._cut_off_time: Optional[int] = None
        self._start_time: Optional[float] = None

        self.valid: Optional[bool] = None
        self.solved: Optional[bool] = None

    def possible_nums_gen(self) -> list[list[list[int]]]:
        """
        Creates a list with all possible numbers for a position (for the whole puzzle).
        :return: None
        """

        list_possible_nums = []

        for i, row in enumerate(self.sudoku_array.array):
            row_list = []
            for i2, num in enumerate(row):
                poss_num: list[int] = []
                if num == 0:
                    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

                    n_row: list[int] = self.sudoku_array.get_row(i)
                    n_column: list[int] = self.sudoku_array.get_column(i2)
                    n_square: list[int] = self.sudoku_array.get_square((3 * (i // 3)) + (i2 // 3))

                    poss_num = list(numbers - set(n_row + n_column + n_square))
                    poss_num.sort()

                row_list.append(poss_num)

            list_possible_nums.append(row_list)

        return list_possible_nums

    def _backtracking_solver(self, fsudoku_array: SudokuArray) -> bool:
        """
        This method solves a sudoku puzzle via backtracking.
        the sudoku_array object is getting change by the method
        :param fsudoku_array: a sudoku_array object
        :return: True if the puzzle is solved else False.
        """

        if self._cut_off_time is None or timer() - self._start_time < self._cut_off_time:  # type: ignore
            row_x, column_x = fsudoku_array.get_next_num_pos()

            if row_x == -1:
                return True
            for x in self.possible_nums[row_x][column_x]:
                if fsudoku_array.is_valid_num(row_x, column_x, x):
                    fsudoku_array.array[row_x][column_x] = x
                    if self._backtracking_solver(fsudoku_array):
                        return True
                    fsudoku_array.array[row_x][column_x] = 0

            return False
        else:
            return False

    def solve(self, cut_off_time: Optional[int] = None):
        self.solved_sudoku_array = copy.deepcopy(self.sudoku_array)

        if cut_off_time is not None:
            self._cut_off_time = cut_off_time
            self._start_time = timer()

        self._backtracking_solver(self.solved_sudoku_array)
        self.valid = self.solved_sudoku_array.is_valid()
        self.solved = False if self.solved_sudoku_array.get_next_num_pos() != [-1, -1] else True


def solve_sudoku(sudoku: s_array, cut_off_time: Optional[int] = None) -> tuple[Optional[s_array], bool, bool]:
    """Solves a sudoku puzzle (via backtracking).

    :param cut_off_time: the amount of time the backtracking solver should run before cutting off standard time is 10s
    :param sudoku: an 9x9 2d list of ints (0-9)
    :return: 2d list with the solve sudoku puzzle, bool if the solve puzzle is valid, bool if the puzzle is solved
    """

    # errors
    if len(sudoku) != 9:
        raise ValueError("wrong size should be 9x9 2d list")

    if not all([True if len(row) == 9 else False for row in sudoku]):
        raise ValueError("wrong size should be 9x9 2d list")

    for x in range(len(sudoku)):
        for y in range(len(sudoku[x])):
            if not isinstance(sudoku[x][y], int):
                raise TypeError(" wrong datatype should only be int")

    if cut_off_time is None:
        cut_off_time = 10

    # errors
    if not isinstance(cut_off_time, int):
        raise TypeError("cut_off_time should only be a positive integer")

    if cut_off_time <= 0:
        raise ValueError("cut_off_time should only be a positive integer")

    sudoku_puzzle = SudokuArray(sudoku)
    game = SudokuSolver(sudoku_puzzle)

    game.solve(cut_off_time)

    return game.solved_sudoku_array.array, game.valid, game.solved  # type: ignore
