class Puzzle2:
    def __init__(self, puzzle_input):
        parsed_content = []
        for x in puzzle_input:
            direction, amount = x.split(" ")
            parsed_content.append((direction, int(amount)))

        self.puzzle_input = parsed_content

    def calculate_position(self):
        horizontal = 0
        depth = 0
        for direction,amount in self.puzzle_input:
            if direction == 'forward':
                horizontal += amount
            elif direction == 'down':
                depth += amount
            elif direction == 'up':
                depth -= amount
        return horizontal*depth

    def calculate_updated_position(self):
        horizontal = 0
        depth = 0
        aim = 0
        for direction,amount in self.puzzle_input:
            if direction == 'forward':
                horizontal += amount
                depth += aim*amount
            elif direction == 'down':
                aim += amount
            elif direction == 'up':
                aim -= amount
        return horizontal*depth
