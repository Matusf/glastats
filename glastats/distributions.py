#!/usr/bin/env python3
from math import erf, sqrt, exp, pi
from statistics import StatisticsError

def norm_cdf(x, precision=4):
    'Cumulative distribution function for the standard normal distribution'
    return round((1.0 + erf(x / sqrt(2.0))) / 2.0, precision)

def norm_pdf(x, precision=4):
    'Probability density function for the standard normal distribution'
    return round(exp((x ** 2) / 2) / sqrt(2 * pi), precision)

def norm_cdf_inv(x, precision=4):
    'Inverse cumulative distribution function for the standard normal distribution'
    if not 0 <= x <= 1:
        raise StatisticsError(('Invalid argument \'{}\' for '
                               'function \'norm_cdf_inv\'').format(x))

    if x == 0: return -float('infinity')
    elif x == 1: return float('infinity')
    elif x < .5:
        return -round(norm_cdf_inv(1 - x), precision)
    return round(sqrt(2) * erf_inv(2 * x - 1), precision)

def erf_inv(x, precision=4):
    'Inverse error function'
    s = 0
    for k in range(1000):
        a = _c_k(k) / (2 * k + 1)
        b = (sqrt(pi) * x / 2) ** (2 * k + 1)
        s += a * b
    return round(s, precision)

def _c_k(k, c={0: 1}):
    'Function for computing coeficients in Inverse error function'
    if k in c:
        return c[k]

    s = 0
    for m in range(k):
        c_m = c.get(m) or _c_k(m)
        c_k_1_m = c.get(k - 1 - m) or _c_k(k - 1 - m)

        if not m in c:
            c[m] = c_m
        if not k - 1 -m in c:
            c[k - 1 - m] = c_k_1_m

        s += ((c_m * c_k_1_m) / ((m + 1) * (2 * m + 1)))
    return s
