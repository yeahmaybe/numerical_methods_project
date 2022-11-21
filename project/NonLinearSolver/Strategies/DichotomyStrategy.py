from .Strategy import Strategy

import numpy as np


class DichotomyStrategy(Strategy):

    __n_iter = 100

    def __get_root_from_segment(self, function, left_border, right_border, precision):
        n_iter = self.__n_iter
        eps = precision
        f = function
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

    def get_roots(self, polynome, left_border, right_border, precision):
        result = []
        f = polynome.as_function

        grid = np.arange(left_border, right_border, precision*1.1)
        points = list(zip(grid, f(grid)))
        for i in range(len(points)-1):
            g = points[i][1] * points[i+1][1]
            if g < 0:
                result.append(self.__get_root_from_segment(
                    function=f,
                    left_border=points[i][0],
                    right_border=points[i+1][0],
                    precision=precision)
                )
        return result








