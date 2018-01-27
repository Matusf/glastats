#!/usr/bin/env python3

import env
import unittest

from glastats import LinearRegression


class TestRegression(unittest.TestCase):
    x = list(range(0, 20, 2))
    y = list(range(0, 10, 1))

    def test_alpha(self):
        reg = LinearRegression(self.x, self.y)
        self.assertEqual(round(reg.alpha, 2), 0)

    def test_beta(self):
        reg = LinearRegression(self.x, self.y)
        self.assertEqual(round(reg.beta, 2), .5)

    def test_prediction(self):
        reg = LinearRegression(self.x, self.y)
        self.assertEqual(reg.predict(50), [25])


if __name__ == '__main__':
    unittest.main()
