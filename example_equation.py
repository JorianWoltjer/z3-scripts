from z3 import *

s = Solver()

# Define variables
x = Real('x')

# Define operations (an equation in this case)
y = 6*x**2 + 11*x - 35

# Define constraints
s.add(y == 0)
# s.add(6*x**2 + 11*x - 35 == 0)  # Also works

if s.check() == sat:  # If satisfiable
    print(s.model())  # [x = 5/3]

# All solutions
# while s.check() == sat:  # While satisfiable
#     m = s.model()
#     print(m)  # [x = 5/3], [x = -7/2]
#     s.add(x != m[x])  # Exclude this solution
