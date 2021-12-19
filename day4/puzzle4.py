class Puzzle4:
    def __init__(self, puzzle_input):
        self.numbers = puzzle_input.split("\n\n")[0].split(",")
        self.boards = [[y.split() for y in x.split("\n")] for x in puzzle_input.split("\n\n")[1:]]
