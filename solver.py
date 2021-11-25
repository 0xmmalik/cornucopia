import z3


class System:
    def __init__(self, symbols):
        self.symbols = symbols
        self.variables = set()
        for dictionary in self.symbols:
            for key in dictionary.coeffs:
                self.variables.add(key)
        self.variables = list(self.variables)
        self.variables.remove(1)
        self.z3vars = [z3.Int(variable) for variable in self.variables]
        self.solver = z3.Solver()

    def solve(self, output):
        for i in range(len(self.symbols)):
            self.solver.add(
                z3.Sum([
                    self.symbols[i].coeffs[self.variables[j]] * self.z3vars[j]
                    for j in range(len(self.variables))
                ]) + self.symbols[i].coeffs[1] == output[i])
        for z3var in self.z3vars:
            self.solver.add(z3.And(0 <= z3var, z3var <= 255))
        if self.solver.check() == z3.sat:
            print(self.solver.model()) # make dis list of ints
