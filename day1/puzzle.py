class Puzzle:
    def __init__(self, puzzle_input):
        # Don't like doing work in the constructor, but I'm lazy
        self.puzzle_input = [int(val) for val in puzzle_input]

    def print_puzzle_input(self):
        print(f"{self.puzzle_input}")

    def calculate_increase(self):
        count = 0
        for i,value in enumerate(self.puzzle_input):
            if len(self.puzzle_input) > (i+1) and self.puzzle_input[i+1] > value:
                count += 1
        return count

    def calculate_window_increase(self):
        count = 0
        for i,value in enumerate(self.puzzle_input):
            if len(self.puzzle_input) <= (i+3):
                return count
            current_window = [value, self.puzzle_input[i+1], self.puzzle_input[i+2]]
            next_window = [self.puzzle_input[i+1], self.puzzle_input[i+2], self.puzzle_input[i+3]]
            if sum(current_window) < sum(next_window):
                count += 1
        return count
