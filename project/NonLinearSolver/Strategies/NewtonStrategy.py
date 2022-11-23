import numpy as np
import decimal as dec
from .Strategy import Strategy
from ..Polynome import Polynome


class NewtonStrategy(Strategy):

    def __get_derivative(self, polynome, x):
        c = polynome.get_coefficients()
        c_new = {0: 0}
        for k in c:
            if k != 0:
                c_new[k-1] = c[k] * k

        p = Polynome(c_new)
        d = p.as_function
        return d(x)

    def get_root(self, polynome, left_border, right_border, precision):
        N_iter = 1000
        eps = precision
        f = polynome.as_function
        d = self.__get_derivative
        c = 1
        x_prev = dec.Decimal(str(left_border))
        x_next = dec.Decimal(x_prev - (c * f(x_prev)))/d(polynome, x_prev)

        while abs(x_next - x_prev) > dec.Decimal(eps) and N_iter > 0:
            g = abs(x_next - x_prev)
            N_iter -= 1
            x_prev = x_next
            f_x = f(x_prev)
            der = d(polynome, x_prev)

            x_next = x_prev - c * f_x / der

        return float(x_next)
