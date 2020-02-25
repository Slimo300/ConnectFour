import unittest

import numpy as np

from Board import Board


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.a = Board(6, 7)

    def test_making_move(self):
        self.a.drop_piece(0, 1)
        self.assertEqual(self.a.get(0, 0), 1)

    def test_is_full(self):
        self.a.board = np.ones((6, 7))
        self.assertTrue(self.a.is_full())

    def test_next_row(self):
        self.a.drop_piece(0, 2)
        self.a.drop_piece(0, 2)
        self.assertEqual(self.a.get_next_open_row(0), 2)

    def test_valid_loc(self):
        for i in range(6):
            self.a.drop_piece(0, 2)
        self.assertFalse(self.a.drop_piece(0, 2))

if __name__ == '__main__':
    unittest.main()
