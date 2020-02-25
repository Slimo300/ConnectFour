import pygame

from GUI.GUIItem import *


class Screen(GUIItem):
    def __init__(self, size, columns, rows):
        super().__init__(size, columns, rows)
        self.screen = pygame.display.set_mode((size * columns, size * rows + int(2.5 * size)))

    def get_screen(self):
        return self.screen

    def get_size(self):
        return self.size

