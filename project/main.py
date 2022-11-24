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
    1: -2
}
polynome = nls.Polynome(coefs)
polynome.print()

solver = nls.Solver()
roots = solver.get_roots(polynome=polynome)
print("Ответ:", roots)

