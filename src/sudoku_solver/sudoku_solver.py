import copy


class sudoku_array:
    def __init__(self, array):
        """

        :param array: 2d (9x9) list of int (0-9)
        """
        self.array = array

    def get_row(self, row):
        """
        This method returns a list with all numbers in a row

        :param row: int 0-8
        :return: list with all ints in the row
        """
        return self.array[row]

    def get_column(self, column):
        """
        This method returns a list with all numbers in a column

        :param column: int 0-8
        :return: list with all ints in the column
               """
        return [row[column] for row in self.array]

    def get_square(self, square):
        """
         This method returns a list with all numbers in a square

        :param square:  int 0-8
        :return: list with all ints in the square
        """
        square_c = [[[0, 3], [0, 3]], [[0, 3], [3, 6]], [[0, 3], [6, 9]], [[3, 6], [0, 3]], [[3, 6], [3, 6]],
                    [[3, 6], [6, 9]], [[6, 9], [0, 3]], [[6, 9], [3, 6]], [[6, 9], [6, 9]]]

        square_array = []

        for row in range(*square_c[square][0]):
            for num in range(*square_c[square][1]):
                square_array.append(self.array[row][num])
        return square_array

    def get_next_num_pos(self):
        """
        This method returns the next position thats empty (value = 0), going form the top to bottom.
        If all positions full [-1,-1] gets returned. [row,column]
        :return: a list with the possion of the next empty value, if none then [-1,-1]
        """

        for i, row in enumerate(self.array):
            for i2, num in enumerate(row):
                if num == 0:
                    return [i, i2]
        return [-1, -1]

    def is_valid_num(self, row, column, number):
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

    def is_valid(self):
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

    def print_sudoku(self):
        """
        Prints the sudoku puzzle.
        :return: None
        """

        print("")

        for index, row in enumerate(self.array):
            if index % 3 == 0 and index != 0:
                print("-" * 22)
            row_ = ""
            for i, num in enumerate(row):
                if i % 3 == 0 and i != 0:
                    row_ += "| "
                if num == 0:
                    num = " "

                row_ += str(num) + " "

            print(row_)

        print("")


class sudoku_solver:
    def __init__(self, c_sudoku_array):
        """

        :param c_sudoku_array: a sudoku_array object
        """
        self.sudoku_array = c_sudoku_array
        self.solved_sudoku_array = []
        self.possible_nums_gen()
        self.solved_sudoku_array = copy.deepcopy(self.sudoku_array)
        self.backtracking_solver(self.solved_sudoku_array)
        self.valid = self.solved_sudoku_array.is_valid()
        self.solved = False if self.solved_sudoku_array.get_next_num_pos() != [-1, -1] else True

    def possible_nums_gen(self):
        """
        Creates a list with all possible numbers for a position (Ffor the whole puzzle).
        :return: None
        """
        self.possible_nums = [[[], [], [], [], [], [], [], [], []] for _ in range(len(self.sudoku_array.array))]

        for i, row in enumerate(self.sudoku_array.array):
            for i2, num in enumerate(row):
                poss_num = []
                if num == 0:
                    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

                    n_row = self.sudoku_array.get_row(i)
                    n_column = self.sudoku_array.get_column(i2)
                    n_square = self.sudoku_array.get_square((3 * (i // 3)) + (i2 // 3))

                    poss_num = list(numbers - set(n_row + n_column + n_square))
                    poss_num.sort()

                self.possible_nums[i][i2] = poss_num

    def backtracking_solver(self, fsudoku_array):
        """
        This method solves a sudoku puzzle via backtracking.
        the sudoku_array object is getting change by the method
        :param fsudoku_array: a sudoku_array object
        :return: True if the puzzle is solved else False.
        """

        row_x, column_x = fsudoku_array.get_next_num_pos()

        if row_x == -1:
            return True
        for x in self.possible_nums[row_x][column_x]:
            if fsudoku_array.is_valid_num(row_x, column_x, x):
                fsudoku_array.array[row_x][column_x] = x
                if self.backtracking_solver(fsudoku_array):
                    return True
                fsudoku_array.array[row_x][column_x] = 0

        return False


def solve_sudoku(sudoku):
    """Solves a sudoku puzzle (via backtracking).

    :param sudoku: an 9x9 2d list of ints (0-9)
    :return: 2d list with the solve sudoku puzzle, bool if the solve puzzle is valid, bool if the puzzle is solved
    """
    sudoku_puzzle = sudoku_array(sudoku)
    game = sudoku_solver(sudoku_puzzle)
    return [game.solved_sudoku_array.array, game.valid, game.solved]
