from .Strategy import Strategy

import numpy as np


class DichotomyStrategy(Strategy):
    __n_iter = 100

    def get_root(self, polynome, left_border, right_border, precision):
        n_iter = self.__n_iter
        eps = precision
        f = polynome.as_function
        x_left, x_right = left_border, right_border
        result = None

        while np.abs(x_right - x_left) > eps and n_iter > 0:
            n_iter -= 1
            x_new = (x_left + x_right) / 2
            if f(x_new) * f(x_right) < 0:
                x_left = x_new
            elif f(x_new) * f(x_left) < 0:
                x_right = x_new
            result = x_new

        return result
