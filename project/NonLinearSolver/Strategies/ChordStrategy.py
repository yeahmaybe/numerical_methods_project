from .Strategy import Strategy
import numpy as np
import decimal as dec


class ChordStrategy(Strategy):
    __N_iter = 1000

    def __get_first_values(self, left_border, right_border, polynome):
        f = polynome.as_function
        x_prev = dec.Decimal(right_border)
        x_cur = dec.Decimal(left_border)
        x_next = dec.Decimal(x_cur - f(x_cur) * ((x_prev - x_cur) / (f(x_prev) - f(x_cur))))
        return x_prev, x_cur, x_next

    def get_root(self, polynome, left_border, right_border, precision=10**(-7)):
        eps = precision
        f = polynome.as_function
        n_iter = self.__N_iter

        x_prev, x_cur, x_next = self.__get_first_values(
            polynome=polynome,
            left_border=left_border,
            right_border=right_border
        )

        while abs(x_next - x_cur) > eps and n_iter > 0:
            n_iter -= 1
            x_prev = x_cur
            x_cur = x_next
            x_next = x_cur - f(x_cur) * ((x_prev - x_cur) / (f(x_prev) - f(x_cur)))

        return x_next
