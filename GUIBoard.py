import pygame

from Board import *

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


def get_rule(x, y):
    if 2 * C4_SIZE + 3 < x < 5 * C4_SIZE-5 and 0 < y < int(C4_SIZE/3):
        return 1
    if 2 * C4_SIZE + 3 < x < 5 * C4_SIZE-5 and int(C4_SIZE/3) < y < int(2 * C4_SIZE/3):
        return 2
    if 2 * C4_SIZE + 3 < x < 5 * C4_SIZE-5 and int(2 * C4_SIZE/3) < y < int(C4_SIZE):
        return 3


class GUIBoard:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((C4_SIZE*C4_COLUMNS, C4_SIZE*C4_ROWS + int(2.5 * C4_SIZE)))
        self.buttonList = [c * C4_SIZE for c in range(C4_COLUMNS + 1)]
        self.radius = int(C4_SIZE / 2 - 5)
        self.board = Board(C4_ROWS, C4_COLUMNS)
        self.width = C4_COLUMNS * C4_SIZE
        self.height = int((C4_ROWS + 1 + 1 / 2) * C4_SIZE)
        self.draw_board()

    def get_board(self):
        return self.board.get_board()

    def get_board_ob(self):
        return self.board

    def get_screen(self):
        return self.screen

    def draw_board(self):
        pygame.draw.rect(self.screen, (255,255,255), (3, 0, 2 * C4_SIZE - 5, C4_SIZE - 5))
        self.label_display("Options", BLACK, (3, 0, 2 * C4_SIZE- 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, BLUE, ((C4_COLUMNS - 2) * C4_SIZE + 3, 0, 2 * C4_SIZE - 5, C4_SIZE - 5))
        self.label_display("RESET", BLACK, ((C4_COLUMNS - 2) * C4_SIZE + 3, 0, 2 * C4_SIZE - 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
        for c in range(C4_COLUMNS):
            pygame.draw.rect(self.screen, LIGHT_GREEN, (c * C4_SIZE + 3, C4_SIZE, C4_SIZE-5, C4_SIZE-5))
        for c in range(C4_COLUMNS):
            for r in range(C4_ROWS):
                pygame.draw.rect(self.screen, BLUE, (c * C4_SIZE, (r+2) * C4_SIZE, C4_SIZE, C4_SIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c * C4_SIZE + C4_SIZE / 2), int((r+1) * C4_SIZE + C4_SIZE + C4_SIZE / 2)), self.radius)
        for c in range(C4_COLUMNS):
            for r in range(C4_ROWS):
                if self.board.get(r, c) == 1:
                    pygame.draw.circle(self.screen, RED, (int(c * C4_SIZE + C4_SIZE / 2), self.height - int((r-1) * C4_SIZE + C4_SIZE)), self.radius)
                elif self.board.get(r, c) == 2:
                    pygame.draw.circle(self.screen, YELLOW, (int(c * C4_SIZE + C4_SIZE / 2), self.height - int((r-1) * C4_SIZE + C4_SIZE)), self.radius)
        for c in range(C4_COLUMNS):
            self.label_display(str(c+1), BLACK, (self.buttonList[c]+3, C4_SIZE, C4_SIZE - 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
        pygame.display.update()

    def label_display(self, text, color, rect, screen, size):
        down_text = pygame.font.Font('freesansbold.ttf', size)
        text_surf, text_rect = self.text_objects(text, down_text, color)
        x = rect[0] + (rect[2] / 2)
        y = rect[1] + (rect[3] / 2)
        text_rect.center = (x, y)
        screen.blit(text_surf, text_rect)

    def reset(self):
        self.board.reset()

    def reset_hovered(self, x, y):
        return self.width - 2 * C4_SIZE < x < self.width and 0 < y < C4_SIZE

    @staticmethod
    def options_hovered(x, y):
        return 0 < x < 2 * C4_SIZE and 0 < y < C4_SIZE

    def options(self, flag):
        if flag:
            pygame.draw.rect(self.screen, (0, 0, 0), (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, C4_SIZE - 5))
            self.draw_board()
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
            self.label_display('All options', BLACK, (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5),
                               self.screen, int(C4_SIZE / 3 - C4_SIZE / 10))
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
            self.label_display("Only diagonal", BLACK,
                               (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5), self.screen, int(C4_SIZE / 3 - C4_SIZE / 10))
            pygame.draw.rect(self.screen, (255, 255, 255), (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
            self.label_display('Only columns and rows', BLACK, (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5,
                                int(C4_SIZE / 3) - 5), self.screen, int(C4_SIZE / 3 - C4_SIZE / 10))
            pygame.display.update()

    @staticmethod
    def are_rules_hovered(x, y):
        return 2 * C4_SIZE + 3 < x < 5 * C4_SIZE-5 and 0 < y < int(C4_SIZE)

    def shut_rules(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, C4_SIZE))
        self.draw_board()

    def rules_hovered(self, x, y):
        rule = get_rule(x, y)
        if rule == 1:
            self.rule1_hovered()
            self.draw_board()
        if rule == 2:
            self.rule2_hovered()
            self.draw_board()
        if rule == 3:
            self.rule3_hovered()
            self.draw_board()

    def rule1_hovered(self):
        pygame.draw.rect(self.screen, (122, 122, 122), (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display('All options', BLACK, (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5),
                           self.screen, int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display("Only diagonal", BLACK,
                           (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5), self.screen,
                           int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display('Only columns and rows', BLACK, (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5,
                                                            int(C4_SIZE / 3) - 5), self.screen,
                           int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.display.update()

    def rule2_hovered(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display('All options', BLACK, (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5),
                           self.screen, int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, (122, 122, 122),
                         (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display("Only diagonal", BLACK,
                           (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5), self.screen,
                           int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display('Only columns and rows', BLACK, (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5,
                                                            int(C4_SIZE / 3) - 5), self.screen,
                           int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.display.update()

    def rule3_hovered(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display('All options', BLACK, (2 * C4_SIZE + 3, 0, 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5),
                           self.screen, int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display("Only diagonal", BLACK,
                           (2 * C4_SIZE + 3, int(C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5), self.screen,
                           int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, (122, 122, 122),
                         (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5, int(C4_SIZE / 3) - 5))
        self.label_display('Only columns and rows', BLACK, (2 * C4_SIZE + 3, int(2 * C4_SIZE / 3), 3 * C4_SIZE - 5,
                                                            int(C4_SIZE / 3) - 5), self.screen,
                           int(C4_SIZE / 3 - C4_SIZE / 10))
        pygame.display.update()

    @staticmethod
    def are_buttons_hovered(posy):
        return C4_SIZE < posy < 2 * C4_SIZE

    def buttons_hovered(self, posx):
        for c in range(C4_COLUMNS):
            if self.buttonList[c] < posx < self.buttonList[c + 1]:
                pygame.draw.rect(self.screen, BLUE, (self.buttonList[c] + 3, C4_SIZE, C4_SIZE - 5, C4_SIZE - 5))
                self.label_display(str(c+1), BLACK, (self.buttonList[c] + 3, C4_SIZE, C4_SIZE - 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
            else:
                pygame.draw.rect(self.screen, LIGHT_GREEN, (self.buttonList[c] + 3, C4_SIZE, C4_SIZE - 5, C4_SIZE - 5))
                self.label_display(str(c+1), BLACK, (self.buttonList[c] + 3, C4_SIZE, C4_SIZE - 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
            pygame.display.update()


    @staticmethod
    def text_objects(text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def piece_dropped(self, col, piece):
        return self.board.drop_piece(col, piece)
