import pdb

class Puzzle5:
    def __init__(self, puzzle_input):
        self.puzzle_input = [Line(x) for x in puzzle_input.split("\n")]

    def calculate_line_overlap(self):
        return 0

class Line:
    def __init__(self, line_input):
        parsed_input = [[int(y) for y in x.split(",")] for x in line_input.split(" -> ")]
        self.coord1 = tuple(parsed_input[0])
        self.coord2 = tuple(parsed_input[1])

    # Need to neaten this up, perhaps with a collection function or two (e.g. reduce)
    def matching_points(self):
        if self.coord1[0] == self.coord2[0]:
            axis = 1
            common_value = self.coord1[0]
        elif self.coord1[1] == self.coord2[1]:
            axis = 0
            common_value = self.coord1[1]
        else:
            return []

        points = []
        for i in range(min(self.coord1[axis], self.coord2[axis]), max(self.coord1[axis], self.coord2[axis])+1):
            if axis == 1:
                points.append((common_value,i))
            else:
                points.append((i,common_value))
        return points
