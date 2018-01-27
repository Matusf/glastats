#!/usr/bin/env python3

from statistics import mean
from .paired_data import sample_covariance, sample_variance


class LinearRegression(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._x_bar = mean(x)
        self._y_bar = mean(y)
        self._beta = self.beta
        self._alpha = self.alpha

    def __repr__(self):
        return 'LinearRegression(alpha={0}, beta={1})'.format(
                round(self.alpha, 4), round(self.beta, 4))

    @property
    def alpha(self):
        return self._y_bar - self.beta * self._x_bar

    @property
    def beta(self):
        return sample_covariance(self.x, self.y) / sample_variance(self.x)

    def predict(self, x, precision=4):
        if not hasattr(x, '__contains__'):
            x = [x]

        return [round(self.alpha + self.beta * x_i, precision) for x_i in x]
