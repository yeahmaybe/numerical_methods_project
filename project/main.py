import NonLinearSolver as nls
import numpy as np


coefs = {
    0: 95,
    1: 1,
    2: -110,
    4: 35,
    5: -5,
    6: -1
}

c = {
    0: 1,
    1: 6,
    2: -15
}

polynome = nls.Polynome(c)
polynome.print()

f = polynome.as_function

solver = nls.Solver()
roots = solver.get_roots(polynome=polynome)
print(roots)

