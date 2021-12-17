import pytest
from pathlib import Path
from puzzle3 import Puzzle3

class TestPuzzle3:
    def test_puzzle_input(self):
        p = Puzzle3(['1001', '0110'])
        assert p.puzzle_input == ['1001', '0110']

    def test_calculate_gamma_epsilon(self):
        data = Path("day3/test_puzzle3_input.txt").read_text().rstrip().split("\n")
        p = Puzzle3(data)
        assert p.calculate_gamma_epsilon() == 198

    def test_calculate_gamma_epsilon_alternative(self):
        data = Path("day3/test_puzzle3_input.txt").read_text().rstrip().split("\n")
        p = Puzzle3(data)
        assert p.calculate_gamma_epsilon_alternative() == 198

    def test_calculate_lifesupport_rating(self):
        data = Path("day3/test_puzzle3_input.txt").read_text().rstrip().split("\n")
        p = Puzzle3(data)
        assert p.calculate_lifesupport_rating() == 230
