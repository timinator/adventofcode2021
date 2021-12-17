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

    def calculate_lifesupport_rating(self):
        print("got here")
        o2_rating = self.calculate_rating('1', max)
        co2_rating = self.calculate_rating('0', min)
        return o2_rating*co2_rating

    def calculate_rating(self, foo, maxminfunc):
        collection = self.puzzle_input
        for i in range(len(self.puzzle_input)):
            values = [x[i] for x in collection]
            g = self.group(values)
            flag = foo if g.get('0') == g.get('1') else maxminfunc(g, key=g.get)
            collection = [x for x in collection if x[i] == flag]
            if len(collection) == 1:
                return int(collection[0],2)
        return int(collection[0],2)
