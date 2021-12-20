import pytest
from pathlib import Path
from puzzle5 import Puzzle5

class TestPuzzle5:
    def test_puzzle_input(self):
        p = Puzzle5()
        assert p.foo == ''
