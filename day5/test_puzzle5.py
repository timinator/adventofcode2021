import pytest
from pathlib import Path
from puzzle5 import Puzzle5,Line

class TestPuzzle5:
    def test_line_input(self):
        l = Line('0,9 -> 5,9')
        assert l.coord1 == (0,9)
        assert l.coord2 == (5,9)

    def test_line_matching_points(self):
        l = Line('0,9 -> 5,9')
        assert l.matching_points() == [(0,9), (1,9), (2,9), (3,9), (4,9), (5,9)]

    def test_calculate_line_overlap(self):
        data = Path("day5/test_puzzle5_input.txt").read_text().rstrip()
        p = Puzzle5(data)
        assert p.calculate_line_overlap() == 5
