import math

class DeltaFinder:
    def deltaSqr(self, a, b, c):
        d = b ^ 2 - 4 * a * c
        if d >= 0:
            return math.sqrt(d);
        else:
            raise Exception
