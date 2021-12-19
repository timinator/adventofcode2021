import pytest
from pathlib import Path
from puzzle4 import Puzzle4

class TestPuzzle4:
    def test_puzzle_input(self):
        p = Puzzle4('7,4,9,5,11\n\n22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19')
        assert p.numbers == ['7','4','9','5','11']
        assert p.boards == [[['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']]]
