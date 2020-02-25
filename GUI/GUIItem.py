import pygame

ORANGE = (255, 165, 0)
LIGHT_GREEN = (102, 255, 102)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 155, 0)


class GUIItem:
    def __init__(self, size, columns, rows):
        self.size = size
        self.columns = columns
        self.rows = rows

    def label_display(self, text, color, rect, screen, size):
        down_text = pygame.font.Font('freesansbold.ttf', size)
        text_surf, text_rect = self.text_objects(text, down_text, color)
        x = rect[0] + (rect[2] / 2)
        y = rect[1] + (rect[3] / 2)
        text_rect.center = (x, y)
        screen.blit(text_surf, text_rect)

    @staticmethod
    def text_objects(text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()