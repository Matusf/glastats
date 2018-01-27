#!/usr/bin/env python3

from decimal import Decimal
from math import exp, log, sqrt
from statistics import mean, variance as sample_variance


def fisher(num, precision=4):
    num = Decimal(num)
    return round(0.5 * log((1 + num) / (1 - num)), precision)


def inverse_fisher(num, precision=4):
    num = Decimal(num)
    return round((exp(2 * num) - 1) / (exp(2 * num) + 1), precision)


def sample_correlation(sxy, sxx, syy, precision=4):
    return round(sxy / sqrt(sxx * syy), precision)


def sample_covariance(x, y, precision=4):
    x_bar = mean(x)
    y_bar = mean(y)
    n = len(x)

    cov = sum((x_i - x_bar) * (y_i - y_bar) for x_i, y_i in zip(x, y)) / (n - 1)
    return round(cov, precision)
