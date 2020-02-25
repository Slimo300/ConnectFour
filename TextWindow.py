import pygame

from GUIBoard import C4_SIZE, C4_ROWS, C4_COLUMNS, ORANGE, RED, YELLOW


class TextWindow:
    colors = [ORANGE, RED, YELLOW]

    def __init__(self):
        pass

    @staticmethod
    def text_objects(text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def next_move_message(self, screen, player):
        self.message_display("Tura gracza " + str(player), self.colors[player], screen)

    def winning_move_message(self, screen, player):
        self.message_display("WYGRAL GRACZ " + str(player), self.colors[player], screen)

    def not_valid_loc_message(self, screen, player):
        self.message_display("Kolumna pelna", self.colors[player], screen)

    def draw_message(self, screen):
        self.message_display("REMIS", self.colors[0], screen)

    def message_display(self, text, color, screen):
        pygame.draw.rect(screen, (0, 0, 0), (0, 8 * C4_SIZE, C4_COLUMNS * C4_SIZE, C4_SIZE / 2))
        down_text = pygame.font.Font('freesansbold.ttf', int(C4_SIZE / 2 - C4_SIZE / 10))
        text_surf, text_rect = self.text_objects(text, down_text, color)
        text_rect.center = ((C4_COLUMNS * C4_SIZE / 2), int(C4_SIZE * (C4_ROWS + (9 / 4))))
        screen.blit(text_surf, text_rect)
