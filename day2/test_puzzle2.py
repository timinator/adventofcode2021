import pytest
from pathlib import Path
from puzzle2 import Puzzle2

class TestPuzzle2:
    def test_puzzle_input(self):
        p = Puzzle2(['forward 2','down 5','up 3'])
        assert p.puzzle_input == [('forward', 2), ('down', 5), ('up', 3)]
