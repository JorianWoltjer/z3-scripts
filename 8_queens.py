from z3 import *

s = Solver()

queens = []

# Create 8 queens
for i in range(8):
    x = Int(f"q{i}_x")
    y = Int(f"q{i}_y")
    s.add(x >= 0, x <= 7) # X Position 1-8
    s.add(y >= 0, y <= 7) # Y Position 1-8
    queens.append((x, y))

# Distinct columns and rows

xs = [queen[0] for queen in queens]
s.add(Distinct(xs))
ys = [queen[1] for queen in queens]
s.add(Distinct(ys))

# Distinct diagonals

diff = [queen[0] - queen[1] for queen in queens]
s.add(Distinct(diff))

print(s.check())
m = s.model()
print(m)

board = [[0]*8 for _ in range(8)]

for queen in queens:
    x, y = queen
    y = m[y].as_long()
    x = m[x].as_long()
    board[y][x] = "1"

for row in board:
    for cell in row:
        print(cell, end=" ")
        
    print()
