class Polynome:
    __coefficients = {}
    __k_max = 0

    def __init__(self, coefficients):
        self.__coefficients = coefficients
        self.__k_max = max(coefficients)
        #print("Создан полином с коэффициентами:", self.__coefficients)

    def as_function(self, x):
        result = None
        coef = self.__coefficients
        for k in coef:
            if result is None: result = 0
            result += coef[k] * (x ** k)
        return result

    def get_k_max(self):
        return self.__k_max

    def get_coefficients(self):
        coefficients = self.__coefficients.copy()
        return coefficients

    def get_coefficients_reversed(self):
        c = self.__coefficients.copy()
        n = self.__k_max

        for k in range(n//2+1):
            if k not in c:
                c[k] = 0
            if n-k not in c:
                c[n-k] = 0

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

    def get_opposed_coefficients(self):
        c = self.__coefficients
        return {k: -c[k] for k in c}

    def print(self):
        coef = self.__coefficients
        for k in coef:
            if coef[k] != 0:
                if (k == 0):
                    print(str(coef[k]), end='')
                elif (k==1):
                    print(' + ' + str(coef[k]) + 'x', end='')
                elif coef[k] < 0:
                    print(' '+str(coef[k]) + 'x^' + str(k), end='')
                elif coef[k] == 1:
                    print('+ x^' + str(k), end='')
                else:
                    print(' + '+ str(coef[k]) + 'x^' + str(k), end='')
        print()