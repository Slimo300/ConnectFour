from GUI.GUIItem import *


class TextWindow(GUIItem):
    colors = [ORANGE, RED, YELLOW]

    def __init__(self, size, columns, rows):
        super().__init__(size, columns, rows)

    def next_move_message(self, screen, player):
        self.message_display("Tura gracza " + str(player), self.colors[player], screen)

    def winning_move_message(self, screen, player):
        self.message_display("WYGRAL GRACZ " + str(player), self.colors[player], screen)

    def not_valid_loc_message(self, screen, player):
        self.message_display("Kolumna pelna", self.colors[player], screen)

    def draw_message(self, screen):
        self.message_display("REMIS", self.colors[0], screen)

    def message_display(self, text, color, screen):
        pygame.draw.rect(screen, (0, 0, 0), (0, 8 * self.size, self.columns * self.size, self.size / 2))
        down_text = pygame.font.Font('freesansbold.ttf', int(self.size / 2 - self.size / 10))
        text_surf, text_rect = self.text_objects(text, down_text, color)
        text_rect.center = ((self.columns * self.size / 2), int(self.size * (self.size + (9 / 4))))
        screen.blit(text_surf, text_rect)
        print("JO PISZO")
