from abc import abstractmethod

from project.NonLinearSolver.Polynome import Polynome


class Strategy(object):

    @abstractmethod
    def get_root(self, polynome, left_border, right_border, precision):
        pass
