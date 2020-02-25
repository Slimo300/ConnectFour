from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, id):
        self.id = id
        self.type = "AI"

    def make_move(self, board, col=0):
        choice = random.randint(0, 6)
        print(choice)
        return board.drop_piece(choice, self.id)
