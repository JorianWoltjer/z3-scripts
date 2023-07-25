from z3 import *

s = Solver()

square = [
    [Int("a"), Int("b"), Int("c")],
    [Int("d"), Int("e"), Int("f")],
    [Int("g"), Int("h"), Int("i")],
]
sum = Int("sum")

# 0-9
for row in square:
    for n in row:
        s.add(0 < n, n < 10)

# Unique
s.add(Distinct([n for row in square for n in row]))

# Horizontal
for row in square:
    s.add(Sum(row) == sum)

# Vertical
for x in range(len(square)):
    s.add(Sum([row[x] for row in square]) == sum)

# Diagonal
s.add(Sum([square[i][i] for i in range(len(square))]) == sum)
s.add(Sum([square[-i-1][i] for i in range(len(square))]) == sum)

if s.check() == sat:
    m = s.model()
    
    print(f"Sum: {m[sum]}")
    
    for y in range(3):
        print()
        
        for x in range(3):
            print(m[square[y][x]], end=" ")

