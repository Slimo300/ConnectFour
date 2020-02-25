import unittest

from AIPlayer import AIPlayer
from GUIBoard import GUIBoard


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.guiboard = GUIBoard()
        self.player = AIPlayer(2)

    def test_making_move(self):
        a = self.player.make_move(self.guiboard)
        self.assertLessEqual(a, 6)
        self.assertGreaterEqual(a, 0)

    def test_array(self):
        arr = self.player.get_mind()
        print(arr)

if __name__ == '__main__':
    unittest.main()
