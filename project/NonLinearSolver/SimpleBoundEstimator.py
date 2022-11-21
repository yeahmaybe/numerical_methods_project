from .BoundEstimator import BoundEstimator


class SimpleBoundEstimator(BoundEstimator):

    def get_bounds(self, polynome, left_border, right_border):
        poly_c = polynome.get_coefficients()

        if poly_c[0] is None:
            poly_c[0] = 0

        max_k = max(poly_c)

        A = abs(poly_c[0])
        B = abs(poly_c[max_k])
        for i, k in enumerate(poly_c):
            if i != max_k:
                A = max(A, abs(poly_c[k]))
            if i != 0:
                B = max(B, abs(poly_c[k]))

        positive_bounds = [max(left_border, 1 / (1 + B / abs(poly_c[0]))), min(1 + A / abs(poly_c[max_k]), right_border)]
        negative_bounds = [max(left_border, -1 - A / abs(poly_c[max_k])), min(right_border, -1 / (1 + B / abs(poly_c[0])))]
        return [positive_bounds, negative_bounds]
