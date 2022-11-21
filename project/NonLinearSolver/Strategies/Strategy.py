from abc import abstractmethod

from project.NonLinearSolver.Polynome import Polynome


class Strategy(object):

    @abstractmethod
    def get_roots(self, polynome, left_border, right_border, precision):
        pass
