class Player:
    def __init__(self, id):
        self.id = id
        self.type = "player"

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def make_move(self, board, col):
        return board.drop_piece(col, self.id)