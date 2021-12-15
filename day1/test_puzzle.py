import pytest
from pathlib import Path
from puzzle import Puzzle

class TestPuzzle:
    def test_puzzle_input(self):
        p = Puzzle(['171','154','155'])
        assert p.puzzle_input == [171,154,155]
    def test_calculate_increase(self):
        data = Path("day1/test_puzzle_input.txt").read_text().rstrip().split("\n")
        p = Puzzle(data)
        assert p.calculate_increase() == 7
    def test_calculate_window_increase(self):
        data = Path("day1/test_puzzle_input.txt").read_text().rstrip().split("\n")
        p = Puzzle(data)
        assert p.calculate_window_increase() == 5
