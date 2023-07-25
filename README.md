# z3-scripts

A collection of scripts using the Z3 Theorem Prover to solve puzzles

## Included

* [example_equation.py](example_equation.py): A simple quadratic equation for Z3 to solve, with a way to get all solutions
* [8_queens.py](8_queens.py): The famous [Eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) where you need to place 8 queens on a chess board without them attacking eachother
* [sudoku_solver.py](sudoku_solver.py): Solves [sudoku](https://nl.wikipedia.org/wiki/Sudoku) puzzles by encoding the sudoku in a list in the script
* [ctf_code_break.py](ctf_code_break.py): Solves a common challenge of "two numbers are correct but in the wrong place", "one is correct and in the right place", etc. puzzles. Where the goal is to find a valid code
* [google_beginners_ctf_logic.py](google_beginners_ctf_logic.py): Solves a logic circuit by encoding it in Z3 functions, to find what input leads to the wanted output
* [magic_square.py](magic_square.py): Create a [Magic Square](https://en.wikipedia.org/wiki/Magic_square) where all lines add up to the same sum, while every number is unique
