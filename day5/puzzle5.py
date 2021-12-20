class Puzzle5:
    def __init__(self, puzzle_input):
        self.puzzle_input = [[y.split(',') for y in x.split(" -> ")] for x in puzzle_input.split("\n")]
