# This is a small lib to solve sudokus

![Tests](https://github.com/andre4k14/sudoku_solver/actions/workflows/tests.yml/badge.svg)

the sudokus are solved via backtracking it can take a while if the sudoku is unsolvable.

To install it simply copy the command below.

You need python 3.9 or higher.
```bash
pip3 install "git+https://github.com/andre4k14/sudoku_solver.git"
```

## How to use it.

### solve_sudoku function

|Parameter|Type|Description|
| :--- | :----: |  ---: |
|sudoku (required)|2d 9x9 list of ints||
|cut_off_time (optional default = 10 [s])|int|the time in seconds the backtracking_solve has time to run before being stop |

and the second optional parameter is the time the programm has to solve the sudoku

```python3
import pprint
from sudoku_solver.sudokusolver import SudokuArray, SudokuSolver
from sudoku_solver import solve_sudoku

sudoku_1 = [[7, 9, 0, 2, 0, 0, 0, 6, 0],
            [2, 0, 0, 4, 0, 3, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 0, 0, 4, 0, 9],
            [0, 0, 2, 8, 0, 4, 7, 0, 0],
            [8, 0, 1, 0, 0, 0, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 6, 0, 8, 0, 0, 3],
            [0, 2, 0, 0, 0, 5, 0, 4, 8]]

solved_sudoku_array, valid, solved = solve_sudoku(sudoku_1, 1)

pprint.pprint(solved_sudoku_array)
print(valid, solved)

# output
"""
[[7, 9, 3, 2, 8, 1, 5, 6, 4],
 [2, 5, 6, 4, 7, 3, 8, 9, 1],
 [1, 8, 4, 5, 9, 6, 2, 3, 7],
 [6, 7, 5, 1, 3, 2, 4, 8, 9],
 [9, 3, 2, 8, 5, 4, 7, 1, 6],
 [8, 4, 1, 9, 6, 7, 3, 5, 2],
 [4, 6, 8, 3, 2, 9, 1, 7, 5],
 [5, 1, 7, 6, 4, 8, 9, 2, 3],
 [3, 2, 9, 7, 1, 5, 6, 4, 8]]
True True
  """
```