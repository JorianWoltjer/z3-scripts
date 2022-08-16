import itertools
from z3 import *


class CodeBreaker():
    def __init__(self, length=3):
        self.s = Solver()
        self.code = IntVector("x", length)
        [self.s.add(0 <= c, c <= 9) for c in self.code]
        
    def correct_right_place(self, digits, n=1):
        assert len(self.code) == len(digits)
        assert n <= len(digits)
        
        self.s.add(Or(
            *[self.code[i] == digits[i] for i in range(len(self.code))]  # Current digit is in the right place
        ))
    
    def correct_wrong_place(self, digits, n=1):
        assert len(self.code) == len(digits)
        assert n <= len(digits)
        
        possibilities = []
        
        for combination in itertools.combinations(range(len(digits)), n):
            combination_conditions = []
            for i in combination:
                combination_conditions.append(And(
                    self.code[i] != digits[i],  # Current digit is not in the right place
                    Or(*[self.code[ii] == digits[i] for ii in range(len(self.code)) if ii != i])  # Could be in any other spot
                ))
                for ii in range(len(self.code)):  # Other digits can't be anywhere in the code
                    if ii not in combination:
                        combination_conditions.append(And(*[self.code[iii] != digits[ii] for iii in range(len(self.code))]))
            
            possibilities.append(And(*combination_conditions))
        
        self.s.add(Or(*possibilities))
        
    def wrong(self, digits):
        assert len(self.code) == len(digits)
        
        for i in range(len(self.code)):
            [self.s.add(self.code[i] != digits[ii]) for ii in range(len(digits))]
            
    def solve(self, verbose=False):
        if verbose: print("Solver:", self.s, sep="\n")

        solutions = []
        while self.s.check() == sat:  # Find all solutions
            m = self.s.model()
            if verbose: print("Model:", m, sep="\n")

            solution = "".join(str(m[c].as_long()) for c in self.code)
            if verbose: print(solution)
            solutions.append(solution)
            
            self.s.add(Or(*[digit != m[digit] for digit in self.code]))  # Exclude this solution in next search
        
        return solutions

breaker = CodeBreaker()

# 682: One is correct and in the right place
breaker.correct_right_place([6, 8, 2], n=1)
# 614: One is correct but in the wrong place
breaker.correct_wrong_place([6, 1, 4], n=1)
# 206: Two are correct but in the wrong place
breaker.correct_wrong_place([2, 0, 6], n=2)
# 738: Nothing is correct
breaker.wrong([7, 3, 8])
# 780: One is correct but in the wrong place
breaker.correct_wrong_place([7, 8, 0], n=1)

print("Solving...")
print("Solutions:", breaker.solve(verbose=False))
