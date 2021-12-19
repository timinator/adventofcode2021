import pytest
from pathlib import Path
from puzzle4 import Puzzle4,Board

class TestPuzzle4:
    def test_puzzle_input(self):
        p = Puzzle4('7,4,9,5,11\n\n22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19')
        assert p.numbers == ['7','4','9','5','11']
        assert p.boards == [[['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']]]

    def test_board_input(self):
        b = Board([['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']])
        assert b.board_input == [['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']]

    # def test_calculate_winning_board_score(self):
    #     p = Puzzle4('7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19\n\n 3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6\n\n14 21 17 24  4\n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n 2  0 12  3  7')
    #     assert p.calculate_winning_board_score() == 4512

    def test_board_match(self):
        b = Board([['22', '13', '17', '11', '0'], ['8', '2', '23', '4', '24'], ['21', '9', '14', '16', '7'], ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']])
        b.new_number('0')
        b.new_number('24')
        b.new_number('7')
        b.new_number('5')
        b.new_number('19')
        assert b.has_match() == True

    def test_board_score(self):
        b = Board([['14', '21', '17', '24', '4'], ['10', '16', '15', '9', '19'], ['18', '8', '23', '26', '20'], ['22', '11', '13', '6', '5'], ['2', '0', '12', '3', '7']])
        b.new_number('7')
        b.new_number('4')
        b.new_number('9')
        b.new_number('5')
        b.new_number('11')
        b.new_number('17')
        b.new_number('23')
        b.new_number('2')
        b.new_number('0')
        b.new_number('14')
        b.new_number('21')
        b.new_number('24')
        assert b.score() == 4512
