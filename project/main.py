import NonLinearSolver as nls
import numpy as np


coefs = {
    1: 1,
    2: -5,
    3: 1,
    4: 5
}

c = {
    0: 1,
    1: -2
}
polynome = nls.Polynome(coefs)
polynome.print()

solver = nls.Solver()
roots = solver.get_roots(polynome=polynome)
print("Ответ:", roots)

