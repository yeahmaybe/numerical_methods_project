from abc import abstractmethod


class BoundEstimator(object):

    @abstractmethod
    def get_bounds(self, polynome,  precision):
        pass