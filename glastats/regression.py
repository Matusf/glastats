#!/usr/bin/env python3

from statistics import mean
from .paired_data import sample_covariance


class LinearRegression(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._alpha = alpha
        self._beta = beta
        self._x_bar = mean(x)
        self._y_bar = mean(y)

    @property
    def alpha(self, x, y):
        return self._y_bar - _beta * self._x_bar

    @property
    def beta(self, x, y):
        return sample_covariance(x, y) / sample_variance(x)

    def fit(self, x, y):
        beta = sample_covariance(x, y) / sample_variance(x)
        alpha = self._y_bar - _beta * self._x_bar

    def plot(self):
        pass
