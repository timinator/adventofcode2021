class Puzzle3:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def calculate_gamma_epsilon(self):
        gamma = ''
        epsilon = ''
        for i in range(len(self.puzzle_input[0])):
            values = [x[i] for x in self.puzzle_input]
            g = self.group(values)
            gamma += max(g, key=g.get)
            epsilon += min(g, key=g.get)
        return int(gamma,2) * int(epsilon,2)

    def calculate_gamma_epsilon_alternative(self):
        gamma = ''
        epsilon = ''
        data = list(zip(*self.puzzle_input))
        for i in range(len(data)):
            g = self.group(data[i])
            gamma += max(g, key=g.get)
            epsilon += min(g, key=g.get)
        return int(gamma,2) * int(epsilon,2)

    def group(self, values):
        d = {}
        for x in values:
            if d.get(x):
                d[x] += 1
            else:
                d[x] = 1
        return d
