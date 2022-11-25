import decimal as dec

from .Polynome import Polynome
from .BoundEstimator import BoundEstimator


class LagrangeBoundEstimator(BoundEstimator):

    def __get_upper_bound(self, coefficients):
        coefs = coefficients

        pn = Polynome(coefs)
        if pn.get_last_coefficient() < 0:
            coefs = pn.get_opposed_coefficients()

        n = pn.get_k_max()

        c_neg = {0: 0}
        for k in coefs:
            if coefs[k] < 0:
                c_neg[k] = coefs[k]

        idx = max(c_neg)
        Cmax = abs(c_neg[min(c_neg, key=c_neg.get)])

        if n == idx:
            return 1

        return float(1 + (abs(Cmax) / coefs[n]) ** dec.Decimal(1 / (n - idx)))

    def get_bounds(self, polynome, precision):
        n = polynome.get_k_max()
        coefs = polynome.get_coefficients()
        r = self.__get_upper_bound(coefs)

        coefs_rev = polynome.get_coefficients_reversed()
        r1 = self.__get_upper_bound(coefs_rev)

        r2 = self.__get_upper_bound(
            {k: coefs[k] if (k % 2 == 0) else -coefs[k] for k in coefs}
        )

        r3 = self.__get_upper_bound(
            {k: coefs_rev[k] if ((n-k) % 2 == 0) else -coefs_rev[k] for k in coefs_rev}
        )

        result = [[-r2, -1/r3], [1/r1, r]]
        if abs(r - 1/r1) < precision:
            result = result[:1]
        if abs(-r2 + 1 / r3) < precision:
            result = result[1:]
        return result
