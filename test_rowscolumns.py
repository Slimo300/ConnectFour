import unittest

from RowsColumnsOnly import RowsColumnsOnly
from Board import Board


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.rules = RowsColumnsOnly()
        self.theBoard = Board(6, 7)

    def test_diagonal(self):
        self.theBoard.drop_piece(0, 1)
        self.theBoard.drop_piece(1, 2)
        self.theBoard.drop_piece(1, 1)
        self.theBoard.drop_piece(2, 2)
        self.theBoard.drop_piece(2, 2)
        self.theBoard.drop_piece(2, 1)
        self.theBoard.drop_piece(3, 2)
        self.theBoard.drop_piece(3, 2)
        self.theBoard.drop_piece(3, 2)
        self.theBoard.drop_piece(3, 1)
        self.assertFalse(self.rules.winning_move(self.theBoard.get_board(), 1, 7, 6))

    def test_horizontal(self):
        self.theBoard.drop_piece(0, 1)
        self.theBoard.drop_piece(0, 1)
        self.theBoard.drop_piece(0, 1)
        self.theBoard.drop_piece(0, 1)
        self.assertTrue(self.rules.winning_move(self.theBoard.get_board(), 1, 7, 6))

    def test_vertical(self):
        self.theBoard.drop_piece(0, 1)
        self.theBoard.drop_piece(1, 1)
        self.theBoard.drop_piece(2, 1)
        self.theBoard.drop_piece(3, 1)
        self.assertTrue(self.rules.winning_move(self.theBoard.get_board(), 1, 7, 6))


if __name__ == '__main__':
    unittest.main()
