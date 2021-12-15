class Puzzle:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def print_puzzle_input(self):
        print(f"{self.puzzle_input}")

    def calculate_increase(self):
        count = 0
        for i,value in enumerate(self.puzzle_input):
            if len(self.puzzle_input) > (i+1) and int(self.puzzle_input[i+1]) > int(value):
                count += 1
        return count
