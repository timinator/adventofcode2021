import pytest
from pathlib import Path
from puzzle import Puzzle

class TestPuzzle:
    def test_puzzle_input(self):
        p = Puzzle("171\n154\n155\n")
        assert p.puzzle_input == "171\n154\n155\n"
    def test_calculate_increase(self):
        data = Path("day1/puzzle_input.txt").read_text()
        p = Puzzle(data)
        assert p.calculate_increase() == 7
