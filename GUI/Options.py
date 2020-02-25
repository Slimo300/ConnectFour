import pygame

from GUI.GUIItem import *


class Options(GUIItem):
    def __init__(self, size, columns, rows):
        super().__init__(size, columns, rows)
        self.width = columns * size

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (3, 0, 2 * self.size - 5, self.size - 5))
        self.label_display("Options", BLACK, (3, 0, 2 * self.size - 5, self.size - 5), screen,
                           int(self.size / 2 - self.size / 10))
        pygame.draw.rect(screen, BLUE, ((self.columns - 2) * self.size + 3, 0, 2 * self.size - 5, self.size - 5))
        self.label_display("RESET", BLACK, ((self.columns - 2) * self.size + 3, 0, 2 * self.size - 5, self.size - 5),
                           screen, int(self.size / 2 - self.size / 10))

    def is_reset_hovered(self, x, y):
        return self.width - 2 * self.size < x < self.width and 0 < y < self.size

    def are_options_hovered(self, x, y):
        return 0 < x < 2 * self.size and 0 < y < self.size

    def options(self, flag, screen):
        if flag:
            pygame.draw.rect(screen, (0, 0, 0), (2 * self.size + 3, 0, 3 * self.size - 5, self.size - 5))
            #self.draw_board()
        else:
            pygame.draw.rect(screen, (255, 255, 255), (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5))
            self.label_display('All options', BLACK, (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5),
                               screen, int(self.size / 3 - self.size / 10))
            pygame.draw.rect(screen, (255, 255, 255),
                             (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
            self.label_display("Only diagonal", BLACK,
                               (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5),
                               screen, int(self.size / 3 - self.size / 10))
            pygame.draw.rect(screen, (255, 255, 255), (2 * self.size + 3, int(2 * self.size / 3),
                                                            3 * self.size - 5, int(self.size / 3) - 5))
            self.label_display('Only columns and rows', BLACK, (2 * self.size + 3, int(2 * self.size / 3),
                                                                3 * self.size - 5, int(self.size / 3) - 5), screen,
                               int(self.size / 3 - self.size / 10))
            pygame.display.update()

    def are_rules_hovered(self, x, y):
        return 2 * self.size + 3 < x < 5 * self.size - 5 and 0 < y < int(self.size)

    def shut_rules(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (2 * self.size + 3, 0, 3 * self.size - 5, self.size))
        #self.draw_board()

    def get_rule(self, x, y):
        if 2 * self.size + 3 < x < 5 * self.size - 5 and 0 < y < int(self.size / 3):
            return 1
        if 2 * self.size + 3 < x < 5 * self.size - 5 and int(self.size / 3) < y < int(2 * self.size / 3):
            return 2
        if 2 * self.size + 3 < x < 5 * self.size - 5 and int(2 * self.size / 3) < y < int(self.size):
            return 3

    def rules_hovered(self, x, y, screen):
        rule = self.get_rule(x, y)
        if rule == 1:
            self.rule1_hovered(screen)
            #self.draw_board()
        if rule == 2:
            self.rule2_hovered(screen)
            #self.draw_board()
        if rule == 3:
            self.rule3_hovered(screen)
            #self.draw_board()

    def rule1_hovered(self, screen):
        pygame.draw.rect(screen, (122, 122, 122), (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display('All options', BLACK, (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5),
                           screen, int(self.size / 3 - self.size / 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display("Only diagonal", BLACK,
                           (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5), screen,
                           int(self.size / 3 - self.size / 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (2 * self.size + 3, int(2 * self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display('Only columns and rows', BLACK, (2 * self.size + 3, int(2 * self.size / 3), 3 * self.size - 5,
                                                            int(self.size / 3) - 5), screen,
                           int(self.size / 3 - self.size / 10))
        pygame.display.update()

    def rule2_hovered(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display('All options', BLACK, (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5),
                           screen, int(self.size / 3 - self.size / 10))
        pygame.draw.rect(screen, (122, 122, 122),
                         (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display("Only diagonal", BLACK,
                           (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5), screen,
                           int(self.size / 3 - self.size / 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (2 * self.size + 3, int(2 * self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display('Only columns and rows', BLACK, (2 * self.size + 3, int(2 * self.size / 3), 3 * self.size - 5,
                                                            int(self.size / 3) - 5), screen,
                           int(self.size / 3 - self.size / 10))
        pygame.display.update()

    def rule3_hovered(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display('All options', BLACK, (2 * self.size + 3, 0, 3 * self.size - 5, int(self.size / 3) - 5),
                           screen, int(self.size / 3 - self.size / 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display("Only diagonal", BLACK,
                           (2 * self.size + 3, int(self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5), screen,
                           int(self.size / 3 - self.size / 10))
        pygame.draw.rect(screen, (122, 122, 122),
                         (2 * self.size + 3, int(2 * self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5))
        self.label_display('Only columns and rows', BLACK,
                           (2 * self.size + 3, int(2 * self.size / 3), 3 * self.size - 5, int(self.size / 3) - 5),
                           screen, int(self.size / 3 - self.size / 10))
        pygame.display.update()