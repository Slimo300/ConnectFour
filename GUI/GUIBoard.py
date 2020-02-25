from GUI.GUIItem import *


class GUIBoard(GUIItem):
    def __init__(self, size, columns, rows):
        super().__init__(size, columns, rows)
        self.radius = int(size / 2 - 5)
        self.width = columns * size
        self.height = int((rows + 1 + 1 / 2) * size)

    def draw(self, screen, board):
        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.rect(screen, BLUE, (c * self.size, (r+2) * self.size, self.size, self.size))
                pygame.draw.circle(screen, BLACK, (int(c * self.size + self.size / 2),
                                                   int((r+1) * self.size + self.size + self.size / 2)), self.radius)
        for c in range(self.columns):
            for r in range(self.rows):
                if board.get(r, c) == 1:
                    pygame.draw.circle(screen, RED, (int(c * self.size + self.size / 2),
                                                     self.height - int((r-1) * self.size + self.size)), self.radius)
                elif board.get(r, c) == 2:
                    pygame.draw.circle(screen, YELLOW, (int(c * self.size + self.size / 2),
                                                        self.height - int((r-1) * self.size + self.size)), self.radius)
