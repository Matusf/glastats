#!/usr/bin/env python3

from decimal import Decimal
from math import exp, log, sqrt
from statistics import mean, variance as sample_variance


def fisher(num, precision=4):
    num = Decimal(num)
    return round(log((1 + num) / (1 - num)), precision)


def inverse_fisher(num, precision=4):
    num = Decimal(num)
    return round((exp(2 * num) - 1) / (exp(2 * num) + 1), 4)


def sample_correlation(sxy, sxx, syy):
    sxy, sxx, syy = Decimal(sxy), Decimal(sxx), Decimal(syy)
    return sxy / sqrt(sxx * sxy)


def sample_covariance(x, y):
    x_bar =  mean(x)
    y_bar =  mean(y)
    n = len(x)

    return sum(x_i * y_i - n * x_bar * y_bar for x_i, y_i in zip(x, y))
