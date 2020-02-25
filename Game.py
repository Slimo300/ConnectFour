import sys
import random
import math

from TextWindow import TextWindow
from Cursor import Cursor
from Player import Player
from GUIBoard import *
from Rules import Rules
from RowsColumnsOnly import RowsColumnsOnly
from DiagonalOnly import DiagonalOnly
from AIPlayer import AIPlayer


class Game:
    def __init__(self):
        self.gui_board = GUIBoard()
        self.cursor = Cursor()
        self.player1 = Player(1)
        self.player2 = AIPlayer(2)
        self.rules = Rules()
        self.textWindow = TextWindow()
        self.currentPlayer = self.assign_player()
        self.gameOver = False
        self.menuFlag = False

    def assign_player(self):
        a = random.randint(0, 1)
        if a == 0:
            self.textWindow.next_move_message(self.gui_board.get_screen(), self.player1.get_id())
            return self.player1
        else:
            self.textWindow.next_move_message(self.gui_board.get_screen(), self.player2.get_id())
            return self.player2

    def switch_players(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
        self.textWindow.next_move_message(self.gui_board.get_screen(), self.currentPlayer.get_id())

    def reset(self):
        self.menuFlag = False
        self.gui_board.reset()

    def change_rules(self, rule):
        if rule == 1:
            self.rules = Rules()
        elif rule == 2:
            self.rules = DiagonalOnly()
        else:
            self.rules = RowsColumnsOnly()
        self.reset()

    def update_cursor(self, event):
        x = event.pos[0]
        y = event.pos[1]
        self.cursor.update(x, y)

    def mouse_motion(self):
        if self.gameOver is False and self.menuFlag is False:
            if self.gui_board.are_buttons_hovered(self.cursor.gety()):
                self.gui_board.buttons_hovered(self.cursor.getx())
            else:
                self.gui_board.draw_board()
        elif self.menuFlag:
            if self.gui_board.are_rules_hovered(self.cursor.getx(), self.cursor.gety()):
                self.gui_board.rules_hovered(self.cursor.getx(), self.cursor.gety())
            else:
                self.gui_board.draw_board()

    def move_made(self):
        if self.rules.winning_move(self.gui_board.get_board(), self.currentPlayer.get_id(), C4_COLUMNS, C4_ROWS):
            self.gameOver = True
            self.textWindow.winning_move_message(self.gui_board.get_screen(), self.currentPlayer.get_id())
        elif self.gui_board.get_board_ob().is_full():
            self.textWindow.draw_message(self.gui_board.get_screen())
            self.gameOver = True
        else:
            self.switch_players()

    def mouse_clicked(self):
        if self.gameOver is False and self.menuFlag is False:
            if self.gui_board.are_buttons_hovered(self.cursor.gety()):
                col = int(math.floor(self.cursor.getx() / C4_SIZE))
                if self.currentPlayer.make_move(self.gui_board, col):
                    self.move_made()
                else:
                    self.textWindow.not_valid_loc_message(self.gui_board.get_screen(), self.currentPlayer.get_id())
            self.gui_board.draw_board()
        elif self.menuFlag:
            if self.gui_board.are_rules_hovered(self.cursor.getx(), self.cursor.gety()):
                rule = get_rule(self.cursor.getx(), self.cursor.gety())
                self.change_rules(rule)
                self.gui_board.shut_rules()
                self.gameOver = self.menuFlag = False
                self.reset()
        if self.gui_board.reset_hovered(self.cursor.getx(), self.cursor.gety()):
            self.gui_board.reset()
            self.assign_player()
            self.gameOver = self.menuFlag = False
        if self.gui_board.options_hovered(self.cursor.getx(), self.cursor.gety()):
            self.gui_board.options(self.menuFlag)
            self.menuFlag = not self.menuFlag
        self.gui_board.draw_board()

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.currentPlayer.get_type() == "player":
                    if event.type == pygame.MOUSEMOTION:
                        self.update_cursor(event)
                        self.mouse_motion()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.update_cursor(event)
                        self.mouse_clicked()
                elif self.currentPlayer.get_type() == "AI":
                    if not self.gameOver and not self.menuFlag:
                        print("AI")
                        if self.currentPlayer.make_move(self.gui_board):
                            self.move_made()
                        else:
                            self.textWindow.not_valid_loc_message(self.gui_board.get_screen(), self.currentPlayer.get_id())
                        self.gui_board.draw_board()
                    else:
                        self.currentPlayer = self.player1


if __name__ == "__main__":
    theGame = Game()
    theGame.start_game()
