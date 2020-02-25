import numpy as np


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns))

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows

    def get(self, row, column):
        return self.board[row][column]

    def get_board(self):
        return self.board

    def drop_piece(self, col, piece):
        if self.is_valid_location(col):
            r = self.get_next_open_row(col)
            self.board[r][col] = piece
            return True
        else:
            return False

    def is_valid_location(self, col):
        return self.board[self.rows - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.rows):
            if self.board[r][col] == 0:
                return r

    def reset(self):
        self.board = np.zeros((self.rows, self.columns))

    def is_full(self):
        for c in range(self.columns):
            if self.board[self.rows-1][c] == 0:
                return False
        return True
