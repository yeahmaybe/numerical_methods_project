from .Strategies.Strategy import Strategy
from .Strategies.DichotomyStrategy import DichotomyStrategy
from .Strategies.ChordStrategy import ChordStrategy
from .Strategies.NewtonStrategy import NewtonStrategy
from .Polynome import Polynome
from .LagrangeBoundEstimator import LagrangeBoundEstimator

import numpy as np
import decimal as dec


class Solver(object):
    __strategy = Strategy()

    def set_strategy(self, strategy):
        self.__strategy = strategy
        return strategy

    def __get_intersections(self, A, B):
        def have_intersection(A, B):
            return not (A[0] > B[1] or A[1] < B[0])

        def get_intersection(A, B):
            return [max(A[0], B[0]), min(A[1], B[1])]

        a = 0
        b = 0
        res = []
        while a < len(A) and b < len(B):
            if have_intersection(A[a], B[b]):
                res.append(get_intersection(A[a], B[b]))

            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1

        return res

    def __assume_root(self, polynome, left_border, right_border, precision):

        f = polynome.as_function
        strategy = Strategy()
        if f(left_border) * f(right_border) < 0:
            strategy = ChordStrategy()
        else:
            strategy = NewtonStrategy()

        self.set_strategy(strategy)
        root = self.__strategy.get_root(
            polynome=polynome,
            precision=precision,
            left_border=left_border - 1.1 * precision,
            right_border=right_border + 1.1 * precision
        )
        return root

    def get_roots(self, polynome, left_border=-np.inf, right_border=np.inf, precision=10 ** (-7)):
        pn = Polynome(polynome.get_coefficients())
        result = []
        firstRound = True
        foundNewRoots = True
        while foundNewRoots and len(pn.get_coefficients(as_list=True)) > 1:

            bound_estimator = LagrangeBoundEstimator()
            estimated_bounds = bound_estimator.get_bounds(
                polynome=pn,
                precision=precision
            )
            interest = [[left_border, right_border]]
            bounds = []
            if firstRound:
                bounds = [[-precision, precision]]
                firstRound = False

            bounds += self.__get_intersections(estimated_bounds, interest)
            #print(bounds)
            foundNewRoots = False
            for bound in bounds:
                if len(pn.get_coefficients(as_list=True)) <= 1:
                    break
                x_new = self.__assume_root(
                    polynome=pn,
                    left_border=bound[0],
                    right_border=bound[1],
                    precision=precision
                )
                new_polynome = pn.extract_root(x_new)
                if new_polynome is not None:
                    result.append(x_new)
                    #print(result)
                    foundNewRoots = True
                while new_polynome is not None:
                    pn = new_polynome
                    new_polynome = pn.extract_root(x_new)

                    #print("Новый полином:")
                    #pn.print()

        result.sort()
        bounded_result = []
        for r in result:
            if left_border < r < right_border:
                bounded_result.append(r)
        return list(map(float, bounded_result))
