import pygame

from GUI.Options import Options
from GUI.TextWindow import TextWindow
from GUI.GUIBoard import GUIBoard
from GUI.Buttons import Buttons
from GUI.Screen import Screen

ORANGE = (255, 165, 0)
LIGHT_GREEN = (102, 255, 102)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 155, 0)

C4_ROWS = 6
C4_COLUMNS = 7
C4_SIZE = 75


class GUI:
    def __init__(self, rows, columns, size, board):
        pygame.init()
        self.options = Options(size, columns, rows)
        self.buttons = Buttons(size, columns, rows)
        self.textWindow = TextWindow(size/2, columns, rows)
        self.gui_board = GUIBoard(size, columns, rows)
        self.screen = Screen(size, columns, rows)
        self.draw_gui(board)

    def get_size(self):
        return self.screen.get_size()

    def draw_gui(self, board):
        self.options.draw(self.screen.get_screen())
        self.buttons.draw(self.screen.get_screen())
        self.gui_board.draw(self.screen.get_screen(), board)
        pygame.display.update()

    def next_move_message(self, player_id):
        self.textWindow.next_move_message(self.screen.get_screen(), player_id)

    def winning_move_message(self, player_id):
        self.textWindow.winning_move_message(self.screen.get_screen(), player_id)

    def not_valid_loc_message(self, player_id):
        self.textWindow.not_valid_loc_message(self.screen.get_screen(), player_id)

    def draw_message(self):
        self.textWindow.draw_message(self.screen.get_screen())

    def are_buttons_hovered(self, posy):
        return self.buttons.are_buttons_hovered(posy)

    def buttons_hovered(self, posx):
        return self.buttons.buttons_hovered(posx, self.screen.get_screen())

    def are_options_hovered(self, posx, posy):
        return self.options.are_options_hovered(posx, posy)

    def options_hovered(self, flag):
        self.options.options(flag, self.screen.get_screen())

    def are_rules_hovered(self, posx, posy):
        return self.options.are_rules_hovered(posx, posy)

    def rules_hovered(self, posx, posy):
        self.options.rules_hovered(posx, posy, self.screen.get_screen())

    def reset_hovered(self, posx, posy):
        return self.options.is_reset_hovered(posx, posy)

    def shut_rules(self):
        self.options.shut_rules(self.screen.get_screen())

    def get_rule(self, posx, posy):
        self.options.get_rule(posx, posy)
