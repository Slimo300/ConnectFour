class Rules:

    def __init__(self):
        self.name = "All options"

    def get_name(self):
        return self.name

    @staticmethod
    def winning_move(board, piece, col, row):
        for c in range(col - 3):
            for r in range(row):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True

        for c in range(col):
            for r in range(row - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        for c in range(col - 3):
            for r in range(row - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True

        for c in range(col - 3):
            for r in range(3, row):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True
