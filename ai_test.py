import unittest

from AIPlayer import AIPlayer
from Board import Board
from Rules.Rules import Rules

class MyTestCase(unittest.TestCase):
    def test_something(self):
        the_board = Board(6, 7)
        rules = Rules()
        player = AIPlayer(2, rules, the_board)

        the_board.drop_piece(3, 1)
        the_board.drop_piece(4, 1)
        the_board.drop_piece(5, 1)
        print(player.eval_window([0,1,1,1], 2))

        center_array = [int(i) for i in list(the_board.get_board()[:, the_board.get_columns() // 2])]
        print(center_array)
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
