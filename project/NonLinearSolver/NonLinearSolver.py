from .Strategies.Strategy import Strategy
from .Strategies.DichotomyStrategy import DichotomyStrategy
from .Polynome import Polynome
from .LagrangeBoundEstimator import LagrangeBoundEstimator


class Solver(object):
    __strategy = Strategy()

    def set_strategy(self, strategy):
        self.__strategy = strategy
        return strategy

    def get_roots(self, polynome, left_border, right_border, precision):
        pn = Polynome(polynome.get_coefficients())
        strategy = DichotomyStrategy()
        bound_estimator = LagrangeBoundEstimator()

        all_bounds = bound_estimator.get_bounds(
            polynome=pn,
            left_border=left_border,
            right_border=right_border,
            precision=precision
        )
        print(all_bounds)
        positive_bounds = all_bounds[0]
        zero_bounds = all_bounds[1]
        negative_bounds = all_bounds[2]

        self.set_strategy(strategy)

        result = []
        for bounds in [positive_bounds, zero_bounds, negative_bounds]:
            roots = self.__strategy.get_roots(
                    polynome=polynome,
                    precision=precision,
                    left_border=bounds[0] - 1.1*precision,
                    right_border=bounds[1] + 1.1*precision
            )

            result += roots

        result.sort()
        return result