from collections import defaultdict


class LinearSymbol:
    def __init__(self, name=None):
        self.coeffs = defaultdict(int)
        if name:
            self.coeffs[name] = 1

    @staticmethod
    def promote(n):
        x = LinearSymbol()
        x.coeffs[1] = n
        return x

    def __mul__(self, other):
        assert isinstance(other, int)
        prod = LinearSymbol()
        for i in self.coeffs:
            prod.coeffs[i] = self.coeffs[i] * other
        return prod

    def __add__(self, other):
        if isinstance(other, int):
            return self + LinearSymbol.promote(other)
        assert isinstance(other, LinearSymbol)
        sum_ = LinearSymbol()
        for i in self.coeffs:
            sum_.coeffs[i] += self.coeffs[i]
        for i in other.coeffs:
            sum_.coeffs[i] += other.coeffs[i]
        return sum_

    def __sub__(self, other):
        return self + other * -1

    def __div__(self, other):
        return self * (1 / other)


class NonDetSymbol:
    def __init__(self, value=None):
        self.values = set()
        if value:
            self.values.add(value)

    @staticmethod
    def promote(n):
        return NonDetSymbol(n)

    def __add__(self, other):
        if isinstance(other, int):
            return self + NonDetSymbol.promote(other)
        assert isinstance(other, NonDetSymbol)
        sum_ = NonDetSymbol()
        for x in self.values:
            for y in other.values:
                sum_.values.add(x + y)
        return sum_

    def __mul__(self, other):
        if isinstance(other, int):
            return self * NonDetSymbol.promote(other)
        assert isinstance(other, NonDetSymbol)
        prod = NonDetSymbol()
        for x in self.values:
            for y in other.values:
                prod.values.add(x * y)
        return prod

    def __sub__(self, other):
        return self + other * -1

    def __div__(self, other):
        return self * (1 / other)



if __name__ == "__main__":
    from functions import *
    symbols = [NonDetSymbol(f'x{i+1}') for i in range(12)]
    x = if_function(symbols)
    for symbol in x:
        print(symbol.coeffs)
    import solver
    n = solver.System(x)
    n.solve([51, 54, 194, 206])
