from Player import Player
from Rules.Rules import Rules
import random
import math


class AIPlayer(Player):
    def __init__(self, id, rules, board):
        self.type = "AI"
        self.id = id
        self.opp_id = 1 if id == 2 else 2
        self.rules = rules
        self.board = board

    def is_ending_move(self, board):
        return Rules.winning_move(board.get_board(), self.id, self.board.get_columns(), self.board.get_rows()) or \
               Rules.winning_move(board.get_board(), self.opp_id, self.board.get_columns(), self.board.get_rows()) or \
               len(self.board.get_valid_locations()) == 0

    def minimax(self, board, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):

        valid_locations = self.board.get_valid_locations()
        if depth == 0 or self.is_ending_move(board):
            if self.is_ending_move(board):
                print(len(self.board.get_valid_locations()))
                if self.rules.winning_move(board.get_board(), self.id, self.board.get_columns(), self.board.get_rows()):
                    return None, 1000000000
                if self.rules.winning_move(board.get_board(), self.opp_id, self.board.get_columns(), self.board.get_rows()):
                    return None, -100000000
                else:
                    return None, 0
            else:
                return None, self.score_position(board.get_board(), self.id)
        elif maximizing_player:
            max_eval = -math.inf
            col = random.choice(valid_locations)
            for c in valid_locations:
                board_copy = board.get_copy()
                board_copy.drop_piece(c, self.id)
                node_col, score = self.minimax(board_copy, depth-1, False, alpha, beta)
                if score > max_eval:
                    max_eval = score
                    col = c
                alpha = max(alpha, max_eval)
                if alpha >= beta:
                    break
            print("Max", col, max_eval)
            return col, max_eval
        else:
            min_eval = math.inf
            col = random.choice(valid_locations)
            for c in valid_locations:
                board_copy = board.get_copy()
                board_copy.drop_piece(c, self.opp_id)
                node_col, score = self.minimax(board_copy, depth-1, True, alpha, beta)
                if score < min_eval:
                    min_eval = score
                    col = c
                beta = min(beta, min_eval)
                if alpha >= beta:
                    break
            print("Min", col, min_eval)
            return col, min_eval

    def score_position(self, board, player_id):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, self.board.get_columns() // 2])]
        center_count = center_array.count(player_id)
        score += center_count * 3

        ## Score Horizontal
        for r in range(self.board.get_rows()):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.board.get_columns() - 3):
                window = row_array[c:c + 4]     # 4 - Window length
                score += self.eval_window(window, player_id)

        ## Score Vertical
        for c in range(self.board.get_columns()):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.board.get_rows() - 3):
                window = col_array[r:r + 4]     # 4 - Window length
                score += self.eval_window(window, player_id)

        ## Score posiive sloped diagonal
        for r in range(self.board.get_rows() - 3):
            for c in range(self.board.get_columns() - 3):
                window = [board[r + i][c + i] for i in range(4)]        # 4 - Window length
                score += self.eval_window(window, player_id)

        for r in range(self.board.get_rows() - 3):
            for c in range(self.board.get_columns() - 3):
                window = [board[r + 3 - i][c + i] for i in range(4)]    # 4 - Window length
                score += self.eval_window(window, player_id)

        return score

    def eval_window(self, window, player_id):
        score = 0
        if player_id == self.id:
            opp_id = self.opp_id
        else:
            opp_id = self.id
        if window.count(player_id) == 4:
            score += 100
        elif window.count(player_id) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player_id) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opp_id) == 3 and window.count(0) == 1:
            score -= 4
        return score

    def make_move(self, board, col=0):
        res_col, minimax_score = self.minimax(board, 3, True, -math.inf, math.inf)
        return board.drop_piece(res_col, self.id)

