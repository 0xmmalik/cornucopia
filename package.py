import z3


class Package:
    def __init__(self, output, variables, pairs):
        self.output = output
        self.variables = variables
        self.pairs = pairs

    def solve(self, context={}):
        s = z3.Solver()
        z3_vars = {k: z3.Int(k) for k in self.variables}
        for key in context:
            if key in self.variables:
                s.add(z3_vars[key] == context[key])

        for exp, conds in self.pairs:
            s.push()
            s.add(exp(**z3_vars) == self.output)
            g = conds(**z3_vars)
            for cond in g:
                s.add(cond)
            if s.check() == z3.sat:
                solution = {
                    key: s.model()[z3_vars[key]].as_long()
                    for key in z3_vars
                }
                new_context = context.copy()
                new_context.update(solution)
                yield new_context
            s.pop()


example1 = Package(8, ['x'], [(lambda x: x + 3, lambda x: [x == 5]),
                              (lambda x: x * 2, lambda x: [x != 5, x < 6])])
contexts = list(example1.solve())

example2 = Package(
    10, ['x', 'y'],
    [(lambda x, y: x + y, lambda x, y: [y >= x]),
     (lambda x, y: y - x, lambda x, y: [y < x, y != 14]),
     (lambda x, y: x * y + 2, lambda x, y: [y < x, y == 14, x - y < 3])])

packs = [example1, example2]
contexts = [{}]
for pack in packs:
    contexts = sum((list(pack.solve(context)) for context in contexts), [])

print(contexts)


def dash(x, y):
    output = []
    if x == 5:
        output.append(x + 3)
    elif x < 6:
        output.append(x * 2)

    if y >= x:
        output.append(x + y)
    elif y != 14:
        output.append(y - x)
    elif x - y < 3:
        output.append(x * y + 2)

    return output


for context in contexts:
    print(f'Testing {context}')
    assert dash(**context) == [8, 10]
    print('Works!')
