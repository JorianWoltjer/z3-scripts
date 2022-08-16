from z3 import *

s = Solver()

# Setup variables

a, b, c, d, e, f, g, h, i, j = Bools('a b c d e f g h i j')

# Setup circuit logic

ab = Not(Or(a, Not(b)))
cd = Or(Not(c), d)
ef = Or(e, Not(f))
gh = And(Not(Or(g, h)), Xor(h, i))
ij = And(i, j)

top = And(ab, Not(Or(cd, ef)))
bottom = And(gh, ij)

s.add(And(top, bottom))

# Execute solver

print(s)
print(s.check())
m = s.model()
print(m)

# Create flag

answers = {
    'a': m[a],
    'b': m[b],
    'c': m[c],
    'd': m[d],
    'e': m[e],
    'f': m[f],
    'g': m[g],
    'h': m[h],
    'i': m[i],
    'j': m[j]
}

flag = 'CTF{'
for letter, value in answers.items():
    if value == True:
        flag += letter.upper()

flag += "}"

print(flag)
