from Player import Player
from GUIBoard import C4_COLUMNS
import random
import numpy as np


class AIPlayer(Player):

    def __init__(self, id):
        self.id = id
        self.type = "AI"
        a = np.ones((1, C4_COLUMNS))
        self.mind = a[0]

    def get_mind(self):
        return self.mind

    def make_move(self, board, col=0):
        choice = random.randint(0, 6)
        print(choice)
        return board.piece_dropped(choice, self.id)
