class Puzzle3:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def calculate_gamma_epsilon(self):
        gamma = ''
        epsilon = ''
        for i in range(len(self.puzzle_input[0])):
            g = self.group(i)
            gamma += max(g, key=g.get)
            epsilon += min(g, key=g.get)
        return int(gamma,2) * int(epsilon,2)

    def group(self, index):
        values = [x[index] for x in self.puzzle_input]
        d = {}
        for x in values:
            if d.get(x):
                d[x] += 1
            else:
                d[x] = 1
        return d
