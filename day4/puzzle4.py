import pdb

class Puzzle4:
    def __init__(self, puzzle_input):
        self.numbers = puzzle_input.split("\n\n")[0].split(",")
        self.boards = [Board([y.split() for y in x.split("\n")]) for x in puzzle_input.split("\n\n")[1:]]

    def calculate_winning_board_score(self):
        for number in self.numbers:
            for b in self.boards:
                b.new_number(number)
                if b.has_match():
                    return b.score()
        return 0

    def calculate_worst_board_score(self):
        matched_boards = []
        for number in self.numbers:
            for b in self.boards:
                b.new_number(number)
                if b.has_match() and b not in matched_boards:
                    matched_boards.append(b)
        return matched_boards[-1].score()

class Board:
    def __init__(self, board_input):
        self.board_input = board_input
        self.match_numbers = []
        self.matches = {
            'r0': 0,
            'r1': 0,
            'r2': 0,
            'r3': 0,
            'r4': 0,
            'c0': 0,
            'c1': 0,
            'c2': 0,
            'c3': 0,
            'c4': 0
        }

    def __eq__(self, other):
        return self.board_input == other.board_input

    def __ne__(self, other):
        return self.board_input != other.board_input

    def new_number(self, number):
        if self.has_match():
            return

        for i,row in enumerate(self.board_input):
            for j,value in enumerate(row):
                if value == number:
                    self.matches['r'+str(i)] += 1
                    self.matches['c'+str(j)] += 1
                    self.match_numbers.append(number)

    def has_match(self):
        return any(value == 5 for value in self.matches.values())

    def score(self):
        all_numbers = [number for numbers in self.board_input for number in numbers]
        unmatched_numbers = set(all_numbers) - set(self.match_numbers)
        unmatched_sum = sum([int(x) for x in unmatched_numbers])
        return int(self.match_numbers[-1]) * unmatched_sum
