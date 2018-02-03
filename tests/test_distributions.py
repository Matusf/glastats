#!/usr/bin/env python3

import env
import unittest

from glastats.distributions import norm_cdf, norm_cdf_inv


class TestDistributions(unittest.TestCase):
    def test_norm_cdf(self):
        self.assertEqual(norm_cdf(.99), 0.8389)

    def test_norm_cdf_inv(self):
        self.assertEqual(norm_cdf_inv(.975), 1.96)

if __name__ == '__main__':
    unittest.main()
