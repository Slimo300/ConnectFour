import unittest

from Game import Game


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_player_assign(self):
        id = self.game.currentPlayer.get_id()
        self.assertTrue(id == 1 or id == 2)

    def test_player_switch(self):
        player = self.game.currentPlayer.get_id()
        self.game.switch_players()
        self.assertNotEqual(player, self.game.currentPlayer.get_id())

    def test_rules_change(self):
        self.game.change_rules(2)
        self.assertEqual(self.game.rules.get_name(), "Diagonal Only")




if __name__ == '__main__':
    unittest.main()
