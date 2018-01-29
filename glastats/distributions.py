#!/usr/bin/env python3
from math import erf, sqrt, exp, pi

def norm_cdf(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def norm_pdf(x):
    'Probability density function for the standard normal distribution'
    return exp((x ** 2) / 2) / sqrt(2 * pi)
