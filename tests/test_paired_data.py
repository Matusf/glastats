#!/usr/bin/env python3

import unittest
import env

from glastats.paired_data import (fisher, inverse_fisher, sample_covariance,
                                  sample_correlation)

class TestPairedData(unittest.TestCase):
    def test_fisher(self):
        self.assertEqual(fisher(0.296), 0.3051)

    def test_inverse_fisher(self):
        self.assertEqual(inverse_fisher(0.3051), 0.296)

    def test_sample_correlation(self):
        self.assertEqual(sample_correlation(5325, 177, 174757), 0.9574)

    def test_sample_covariance(self):
        x = [2.1, 2.5, 4.0, 3.6]
        y = [8, 12, 14, 10]

        self.assertEqual(sample_covariance(x, y), 1.5333)

if __name__ == '__main__':
    unittest.main()
