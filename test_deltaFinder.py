from unittest import TestCase
from EquationDelta import DeltaFinder

class TestDeltaFinder(TestCase):
    def test_deltaSqr(self):
        self.fail()
    def test_neg_delta(self):
        d = DeltaFinder
        self.assertRaises(Exception, d.deltaSqr(2, 1, 2))
