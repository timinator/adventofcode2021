import pdb

class Puzzle5:
    def __init__(self, puzzle_input):
        self.lines = [Line(x) for x in puzzle_input.split("\n")]

    def calculate_line_overlap(self):
        grid = self.build_grid()
        return self.find_overlap_count(grid)

    def build_grid(self):
        grid = {}
        for line in self.lines:
            for point in line.matching_points():
                if grid.get(point):
                    grid[point] += 1
                else:
                    grid[point] = 1
        return grid

    def find_overlap_count(self, grid):
        count = 0
        for key, value in grid.items():
            if value >= 2:
                count += 1
        return count

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
            return self.diagonal_points()

        points = []
        for i in range(min(self.coord1[axis], self.coord2[axis]), max(self.coord1[axis], self.coord2[axis])+1):
            if axis == 1:
                points.append((common_value,i))
            else:
                points.append((i,common_value))
        return points

    def diagonal_points(self):
        matching = (self.coord1[0] - self.coord2[0]) == (self.coord1[1] - self.coord2[1])
        starting_point = min(self.coord1, self.coord2) # uses first value in tuple as default
        points = [starting_point]
        while points[-1] != max(self.coord1, self.coord2):
            if matching:
                points.append((points[-1][0]+1, points[-1][1]+1))
            else:
                points.append((points[-1][0]+1, points[-1][1]-1))
        return points
