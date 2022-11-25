import numpy as np
import decimal as dec
def power(x, k):
    res = 1
    for i in range(k):
        res *= x
    return res
class Polynome:
    __coefficients = {}
    __k_max = 0

    def __init__(self, coefficients):
        c = coefficients.copy()
        self.__coefficients = {}
        for k in c:
            if c[k] != 0:
               self.__coefficients[k] = dec.Decimal(c[k])
        self.__k_max = max(coefficients)
        # print("Создан полином с коэффициентами:", self.__coefficients)

    def as_function(self, x):
        result = None
        coef = self.__coefficients
        for k in coef:
            if result is None: result = 0
            result += dec.Decimal(coef[k]) * dec.Decimal(power(x, k))
        return result

    def get_k_max(self):
        return self.__k_max

    def get_coefficients(self, as_list=False, reversed=False):
        c = self.__coefficients.copy()
        if not as_list:
            coefficients = c
        else:
            coefficients = [c[k] if k in c else 0 for k in range(int(self.get_k_max()) + 1)]

        if reversed and not as_list:
            coefficients = Polynome(coefficients).get_coefficients_reversed()
        elif reversed and as_list:
            coefficients = coefficients[::-1]

        return coefficients

    def get_coefficients_reversed(self):
        c = self.__coefficients.copy()
        n = self.__k_max

        for k in range(n // 2 + 1):
            if k not in c:
                c[k] = 0
            if n - k not in c:
                c[n - k] = 0

            c[k], c[n - k] = c[n - k], c[k]

        c_new = {}
        for k in c:
            if c[k] != 0:
                c_new[k] = c[k]

        return c_new

    def get_last_coefficient(self):
        c = self.__coefficients.copy()
        k = self.__k_max
        return c[k]

    def get_zero_coefficient(self):
        c = self.__coefficients.copy()
        if 0 in c:
            return c[0]
        else:
            return 0

    def get_opposed_coefficients(self):
        c = self.__coefficients
        return {k: -c[k] for k in c}

    def print(self):
        coef = self.__coefficients
        for k in coef:
            if coef[k] != 0:
                if (k == 0):
                    print(' + ' + str(coef[k]), end='')
                elif (k == 1):
                    print(' + ' + str(coef[k]) + 'x', end='')
                elif coef[k] < 0:
                    print(' ' + str(coef[k]) + 'x^' + str(k), end='')
                elif coef[k] == 1:
                    print('+ x^' + str(k), end='')
                else:
                    print(' + ' + str(coef[k]) + 'x^' + str(k), end='')
        print()

    def extract_root(self, x):
        x = dec.Decimal(x)
        eps = 10e-6
        c = list(map(dec.Decimal, self.get_coefficients(as_list=True, reversed=True)))
        c_prev = dec.Decimal(0)

        res = []
        n = len(c)
        for i in range(0, n-1):
            c_new = c[i] + x * c_prev
            res.append(c_new)
            c_prev = c_new

        remnant = c_prev * x + dec.Decimal(c[-1])
        if abs(remnant) > eps:
            return None
        else:
            p_res = {}
            for k in range(0, len(res)):
                if res[k] != 0:
                    p_res[len(res)-1-k] = res[k]

            return Polynome(p_res)
