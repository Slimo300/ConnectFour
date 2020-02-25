import sys
import random
import math

from Cursor import Cursor
from Player import Player
from GUIBoard import *
from Rules.Rules import Rules
from Board import Board
from Rules.RowsColumnsOnly import RowsColumnsOnly
from Rules.DiagonalOnly import DiagonalOnly
from AIPlayer import AIPlayer
from GUI.GUI import GUI

ROWS = 6
COLUMNS = 7
SIZE = 75


class Game:
    def __init__(self):
        self.board = Board(ROWS, COLUMNS)
        self.gui = GUI(ROWS, COLUMNS, SIZE, self.board)
        self.cursor = Cursor()
        self.player1 = Player(1)
        self.player2 = AIPlayer(2)
        self.rules = Rules()
        self.currentPlayer = self.assign_player()
        self.gameOver = False
        self.menuFlag = False

    def assign_player(self):
        a = random.randint(0, 1)
        if a == 0:
            self.gui.next_move_message(self.player1.get_id())
            return self.player1
        else:
            self.gui.next_move_message(self.player2.get_id())
            return self.player2

    def switch_players(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
        self.gui.next_move_message(self.currentPlayer.get_id())

    def reset(self):
        self.menuFlag = False
        self.board.reset()

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
            if self.gui.are_buttons_hovered(self.cursor.gety()):
                self.gui.buttons_hovered(self.cursor.getx())
            else:
                self.gui.draw_gui(self.board)
        elif self.menuFlag:
            if self.gui.are_rules_hovered(self.cursor.getx(), self.cursor.gety()):
                self.gui.rules_hovered(self.cursor.getx(), self.cursor.gety())
            else:
                self.gui.draw_gui(self.board)

    def move_made(self):
        if self.rules.winning_move(self.board.get_board(), self.currentPlayer.get_id(), self.board.get_columns(),
                                   self.board.get_rows()):
            self.gameOver = True
            self.gui.winning_move_message(self.currentPlayer.get_id())
        elif self.board.is_full():
            self.gui.draw_message()
            self.gameOver = True
        else:
            self.switch_players()

    def mouse_clicked(self):
        if self.gameOver is False and self.menuFlag is False:
            if self.gui.are_buttons_hovered(self.cursor.gety()):
                col = int(math.floor(self.cursor.getx() / self.gui.get_size()))
                if self.currentPlayer.make_move(self.board, col):
                    self.move_made()
                else:
                    self.gui.not_valid_loc_message(self.currentPlayer.get_id())
            self.gui.draw_gui(self.board)
        elif self.menuFlag:
            if self.gui.are_rules_hovered(self.cursor.getx(), self.cursor.gety()):
                rule = self.gui.get_rule(self.cursor.getx(), self.cursor.gety())
                self.change_rules(rule)
                self.gui.shut_rules()
                self.gameOver = self.menuFlag = False
                self.reset()
        if self.gui.reset_hovered(self.cursor.getx(), self.cursor.gety()):
            self.board.reset()
            self.assign_player()
            self.gameOver = self.menuFlag = False
        if self.gui.are_options_hovered(self.cursor.getx(), self.cursor.gety()):
            self.gui.options_hovered(self.menuFlag)
            self.menuFlag = not self.menuFlag
        self.gui.draw_gui(self.board)

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
                        if self.currentPlayer.make_move(self.board, 0):
                            self.move_made()
                        else:
                            self.gui.not_valid_loc_message(self.currentPlayer.get_id())
                        self.gui.draw_gui(self.board)
                    else:
                        self.currentPlayer = self.player1


if __name__ == "__main__":
    theGame = Game()
    theGame.start_game()
