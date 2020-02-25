from GUI.GUIItem import *

import pygame


class Buttons(GUIItem):
    def __init__(self, size, rows, columns):
        super().__init__(size, rows, columns)
        self.buttonList = [c * self.size for c in range(self.columns + 1)]

    def draw(self, screen):
        for c in range(self.columns):
            pygame.draw.rect(screen, LIGHT_GREEN, (c * self.size + 3, self.size, self.size - 5, self.size - 5))
        for c in range(self.columns):
            self.label_display(str(c + 1), BLACK, (self.buttonList[c] + 3, self.size, self.size - 5, self.size - 5),
                               screen, int(self.size / 2 - self.size / 10))

    def are_buttons_hovered(self, posy):
        return self.size < posy < 2 * self.size

    def buttons_hovered(self, posx, screen):
        for c in range(self.columns):
            if self.buttonList[c] < posx < self.buttonList[c + 1]:
                pygame.draw.rect(screen, BLUE, (self.buttonList[c] + 3, self.size, self.size - 5, self.size - 5))
                self.label_display(str(c+1), BLACK, (self.buttonList[c] + 3, self.size, self.size - 5, self.size - 5),
                                   screen, int(self.size / 2 - self.size / 10))
            else:
                pygame.draw.rect(screen, LIGHT_GREEN, (self.buttonList[c] + 3, self.size, self.size - 5, self.size - 5))
                self.label_display(str(c+1), BLACK, (self.buttonList[c] + 3, self.size, self.size - 5, self.size - 5),
                                   screen, int(self.size / 2 - self.size / 10))
            pygame.display.update()

