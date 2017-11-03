from unittest import TestCase
from ceilp.bugcal import Solver


class TestSolver(TestCase):
    def test_calculate(self):
        self.assertEqual(Solver.calculate(12, 9), 11)
        self.assertEqual(Solver.calculate(25, 25), 40)
        self.assertEqual(Solver.calculate(25, 24), 49)
        self.assertEqual(Solver.calculate(999999999, 999999999), 1999999988)
