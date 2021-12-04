import pytest
from sudoku_solver import solve_sudoku as sus
from sudoku_solver.sudokusolver import SudokuArray, SudokuSolver
import copy

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

test_6 = [[7, 9, 0, 2, 0, 0, 0, 6, 0],  # wrong shape
          [2, 0, 0, 4, 0, 3, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 0, 0, 4, 0, 9],
          [0, 0, 2, 8, 0, 4, 7, 0, 0],
          [8, 0, 1, 0, 0, 0, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [5, 0, 0, 6, 0, 8, 0, 0, 3]]

test_7 = [[7, 9, 0, 2, 0, 0, 0, 6],  # wrong shape
          [2, 0, 0, 4, 0, 3, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 0, 0, 4, 0, 9],
          [0, 0, 2, 8, 0, 4, 0, 0],
          [8, 0, 1, 0, 0, 0, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [5, 0, 0, 6, 8, 0, 0, 3],
          [8, 0, 1, 0, 0, 0, 0, 5, 0]]

test_8 = [["5", "0", "0", "4", "0", "0", "0", "0", "9"],  # wrong type
          [0, 0, 2, 1, 4, 5, 0, 8, 3],
          [0, 3, 6, 2, 0, 9, 0, 0, 5],
          [8, 0, 0, 0, 6, 0, 2, 0, 9],
          [7, 0, 0, 8, 1, 0, 3, 4, 6],
          [0, 6, 3, 0, 9, 4, 0, 0, 1],
          [0, 1, 4, 0, 0, 8, 5, 0, 7],
          [0, 9, 0, 0, 3, 0, 0, 0, 0],
          [3, 0, 0, 0, 5, 0, 9, 6, 8]]

test_9 = [[9.234, 0.2134, 0.3456, 0.456, 0.3645, 0, 4, 0, 7],  # wrong type
          [0, 0, 2, 1, 4, 5, 0, 8, 3],
          [0, 3, 6, 2, 0, 9, 0, 0, 5],
          [8, 0, 0, 0, 6, 0, 2, 0, 9],
          [7, 0, 0, 8, 1, 0, 3, 4, 6],
          [0, 6, 3, 0, 9, 4, 0, 0, 1],
          [0, 1, 4, 0, 0, 8, 5, 0, 7],
          [0, 9, 0, 0, 3, 0, 0, 0, 0],
          [3, 0, 0, 0, 5, 0, 9, 6, 8]]

test_10 = [[0, 0, 2, 1, 4, 5, 0, 8, 3],  # wrong type
           [0, 0, 2, 1, 4, 5, 0, 8, 3],
           [[0], 0, 2, 0, 0, 0, 0, 5, 0],
           [5, 6, 2, 0, 4, 9, 0, 0, 0],
           [0, 7, 0, 0, 6, 3, 0, 0, 0],
           [0, 3, 0, 7, 0, 0, 6, 0, 8],
           [2, 0, 0, 1, 3, 6, 0, 7, 5],
           [0, 0, 5, 9, 0, 8, 2, 0, 0],
           [0, 8, 3, 0, 0, 4, 9, 1, 0]]

test_11 = [[0, 0, 2, 1, 4, 5, 0, 8, 3],  # wrong type
           [0, 0, 2, 1, 4, 5, 0, 8, 3],
           [0, tuple([0]), tuple([0]), 0, 0, 0, 0, 5, 0],
           [0, 7, 0, 0, 6, 3, 0, 0, 0],
           [0, 7, 0, 0, 6, 3, 0, 0, 0],
           [0, 3, 0, 7, 0, 0, 6, 0, 8],
           [2, 0, 0, 1, 3, 6, 0, 7, 5],
           [0, 0, 5, 9, 0, 8, 2, 0, 0],
           [0, 8, 3, 0, 0, 4, 9, 1, 0]]

test_12 = [[0, 0, 2, 1, 4, 5, 0, 8, 3],  # wrong type
           [0, 0, 2, 1, 4, 5, 0, 8, 3],
           [0, 7, 0, 0, 6, 3, 0, 0, 0],
           [{6}, {"num": "0", "num2": 0}, 2, 0, 4, 9, 0, 0, 0],
           [0, 7, 0, 0, 6, 3, 0, 0, 0],
           [0, 3, 0, 7, 0, 0, 6, 0, 8],
           [2, 0, 0, 1, 3, 6, 0, 7, 5],
           [0, 0, 5, 9, 0, 8, 2, 0, 0],
           [0, 8, 3, 0, 0, 4, 9, 1, 0]]

test_13 = [[7, 9, 0, 2, 0, 0, 0, 6],  # wrong shape and wrong type
           [2, 0, 0, 4, 0, 3, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 7, 0, 0, 0, 0, 4, 0, 9],
           [0, 0, 2, 8, 0, 4, 0, 0],
           [8, 0, 1, 0, 0, 0, 0, 5, 0],
           [0, 0, 0, 0, [0], 0, 0, 0],
           [5, 0, 0, 6, 8, 0, 0, 3],
           ["5", 0, 1, 0, 0, 0, 0, 5, 0]
           ]


@pytest.mark.parametrize("test", [test_1, test_2, test_3])
def test_sudoku_array(test):
    t = sus(test)
    assert t[1]


@pytest.mark.parametrize("test", [test_1, test_2, test_3])
def test_with_time_limit_sudoku_array(test):
    t = sus(test, 1)
    assert t[1]


def test_create_representation_sudoku_methode():
    list_true = []
    s_array = copy.deepcopy(test_4)
    for x in range(9):
        for y in range(9):
            for z in range(9):
                s_array[x][y] = z + 1
                s_ary_cls = SudokuArray(s_array)
                string_array = s_ary_cls.create_representation_sudoku()
                new_string_array = ""
                for r in range(11):
                    if not (r == 3 or r == 7):
                        sub_string = string_array[r * 22:r * 22 + 21]
                        for c in range(11):
                            if not (l_st := sub_string[(c * 2):(c * 2 + 1)]) == "|":
                                new_string_array += l_st

                a = x * 9 + y

                if new_string_array[a:a + 1] == str(z + 1):
                    list_true.append(True)
                else:
                    list_true.append(False)

                s_array[x][y] = 0

    assert all(list_true)


def test_print_sudoku_methode(capture_stdout):
    sary = SudokuArray(test_4)
    sary.print_sudoku()
    assert capture_stdout["stdout"] == f"\n{sary.create_representation_sudoku()}\n"


@pytest.mark.parametrize("test", [test_6, test_7, test_13])
def test_invalid_shape(test):
    with pytest.raises(ValueError):
        sus(test)


@pytest.mark.parametrize("test", [test_8, test_9, test_10, test_11, test_12])
def test_invalid_type(test):
    with pytest.raises(TypeError):
        sus(test)


@pytest.mark.parametrize("test,time", [(test_1, "2"), (test_2, 23.4), (test_3, [32, 2345])])
def test_with_wrong_time_limit_sudoku_array(test, time):
    with pytest.raises(TypeError):
        sus(test, time)


@pytest.mark.parametrize("test,time", [(test_3, -1)])
def test_with_wrong_time_limit_sudoku_array2(test, time):
    with pytest.raises(ValueError):
        sus(test, time)


def test_without_time_limit():
    sudoku = SudokuArray(test_3)
    sudoku_s = SudokuSolver(sudoku)
    sudoku_s.solve()


def test_unsolvable():
    sudoku = SudokuArray(test_5)
    sudoku_s = SudokuSolver(sudoku)
    sudoku_s.solve(5)
