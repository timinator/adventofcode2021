import pytest
from pathlib import Path
from puzzle2 import Puzzle2

class TestPuzzle2:
    def test_puzzle_input(self):
        p = Puzzle2(['forward 2','down 5','up 3'])
        assert p.puzzle_input == [('forward', 2), ('down', 5), ('up', 3)]

    def test_calculate_position(self):
        data = Path("day2/test_puzzle2_input.txt").read_text().rstrip().split("\n")
        p = Puzzle2(data)
        assert p.calculate_position() == 150

    def test_calculate_updated_position(self):
        data = Path("day2/test_puzzle2_input.txt").read_text().rstrip().split("\n")
        p = Puzzle2(data)
        assert p.calculate_updated_position() == 900
