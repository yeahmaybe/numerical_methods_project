import NonLinearSolver as nls
import numpy as np

solver = nls.Solver()
coefs = {
    0: 5.826,
    1: 1,
    2: -10,
    4: 3,
    5: 0.5
}
polynome = nls.Polynome(coefs)
polynome.print()

roots = solver.get_roots(
    polynome=polynome,
    left_border=-1,
    right_border=1.2,
    precision=10**(-6)
)
print(roots)

