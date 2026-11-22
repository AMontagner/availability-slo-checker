import unittest
from fractions import Fraction

from slo import evaluate


class SloTest(unittest.TestCase):
    def test_exact_budget_boundary(self):
        target = Fraction("0.999")
        self.assertEqual(evaluate(10000, 10, target), (target, 1, 0))

    def test_exhausted_budget(self):
        _, burn, remaining = evaluate(10000, 25, Fraction("0.999"))
        self.assertEqual((burn, remaining), (Fraction(5, 2), -15))

    def test_fractional_budget_rounds_down(self):
        self.assertEqual(evaluate(999, 1, Fraction("0.999"))[2], -1)

    def test_invalid_counts(self):
        for total, failed in [(0, 0), (10, -1), (10, 11)]:
            with self.subTest(total=total, failed=failed):
                with self.assertRaises(ValueError):
                    evaluate(total, failed, Fraction("0.999"))
