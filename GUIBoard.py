import pygame

class GUIBoard:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((C4_SIZE*C4_COLUMNS, C4_SIZE*C4_ROWS + int(2.5 * C4_SIZE)))
        self.radius = int(C4_SIZE / 2 - 5)
        self.width = C4_COLUMNS * C4_SIZE
        self.height = int((C4_ROWS + 1 + 1 / 2) * C4_SIZE)
        self.draw_board()

    def get_screen(self):
        return self.screen

    def draw_gui(self, board):
        pygame.draw.rect(self.screen, (255,255,255), (3, 0, 2 * C4_SIZE - 5, C4_SIZE - 5))
        self.label_display("Options", BLACK, (3, 0, 2 * C4_SIZE- 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
        pygame.draw.rect(self.screen, BLUE, ((C4_COLUMNS - 2) * C4_SIZE + 3, 0, 2 * C4_SIZE - 5, C4_SIZE - 5))
        self.label_display("RESET", BLACK, ((C4_COLUMNS - 2) * C4_SIZE + 3, 0, 2 * C4_SIZE - 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
        for c in range(C4_COLUMNS):
            pygame.draw.rect(self.screen, LIGHT_GREEN, (c * C4_SIZE + 3, C4_SIZE, C4_SIZE-5, C4_SIZE-5))
        for c in range(C4_COLUMNS):
            self.label_display(str(c+1), BLACK, (self.buttonList[c]+3, C4_SIZE, C4_SIZE - 5, C4_SIZE - 5), self.screen, int(C4_SIZE / 2 - C4_SIZE / 10))
        pygame.display.update()

    def draw_board(self, board):
        for c in range(C4_COLUMNS):
            for r in range(C4_ROWS):
                pygame.draw.rect(self.screen, BLUE, (c * C4_SIZE, (r+2) * C4_SIZE, C4_SIZE, C4_SIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c * C4_SIZE + C4_SIZE / 2), int((r+1) * C4_SIZE + C4_SIZE + C4_SIZE / 2)), self.radius)
        for c in range(C4_COLUMNS):
            for r in range(C4_ROWS):
                if board.get(r, c) == 1:
                    pygame.draw.circle(self.screen, RED, (int(c * C4_SIZE + C4_SIZE / 2), self.height - int((r-1) * C4_SIZE + C4_SIZE)), self.radius)
                elif board.get(r, c) == 2:
                    pygame.draw.circle(self.screen, YELLOW, (int(c * C4_SIZE + C4_SIZE / 2), self.height - int((r-1) * C4_SIZE + C4_SIZE)), self.radius)

