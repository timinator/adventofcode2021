import pytest
from pathlib import Path
from puzzle5 import Puzzle5

class TestPuzzle5:
    def test_puzzle_input(self):
        p = Puzzle5('0,9 -> 5,9\n8,0 -> 0,8')
        assert p.puzzle_input == [[['0','9'], ['5','9']], [['8','0'], ['0','8']]]
