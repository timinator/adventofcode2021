class Puzzle2:
    def __init__(self, puzzle_input):
        parsed_content = []
        for x in puzzle_input:
            direction, amount = x.split(" ")
            parsed_content.append((direction, int(amount)))
        self.puzzle_input = parsed_content
