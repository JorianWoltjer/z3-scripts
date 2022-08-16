from z3 import *

s = Solver()
SIZE = 9

# Create board
sudoku = []
for y in range(SIZE):
    row = Ints(' '.join(f"x{x}y{y}" for x in range(SIZE)))
    sudoku.append(row)

# Range 1-9
for row in sudoku:
    for cell in row:
        s.add(cell >= 1, cell <= 9)

# Each row is distinct
for row in sudoku:
    s.add(Distinct(row))
    
# Each column is distinct
for x in range(SIZE):
    col = []
    for y in range(SIZE):
        col.append(sudoku[y][x])
        
    s.add(Distinct(col))

# Each 3x3 square is distinct
for y in range(SIZE // 3):
    for x in range(SIZE // 3):
        square = []
        for row in sudoku[y*3:(y+1)*3]:
            square += row[x*3:(x+1)*3]
        
        s.add(Distinct(square))

# Setup fixed cells (0=empty)
fixed = [
    [0,0,0,0,9,4,0,3,0],
    [0,0,0,5,1,0,0,0,7],
    [0,8,9,0,0,0,0,4,0],
    [0,0,0,0,0,0,2,0,8],
    [0,6,0,2,0,1,0,5,0],
    [1,0,2,0,0,0,0,0,0],
    [0,7,0,0,0,0,5,2,0],
    [9,0,0,0,6,5,0,0,0],
    [0,4,0,9,7,0,0,0,0],
]

for y in range(SIZE):
    for x in range(SIZE):
        if fixed[y][x] != 0:
            s.add(sudoku[y][x] == fixed[y][x])


# Solve

print(s.check())
m = s.model()

print(m)

# Show solution

for y in range(SIZE):
    for x in range(SIZE):
        print(m[sudoku[y][x]], end=" ")
    
    print()
