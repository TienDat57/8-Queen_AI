import pygame
import sys
from pygame.locals import *

pygame.display.set_caption('8 Queens Problem')
Icon = pygame.image.load('queen.png')
pygame.display.set_icon(Icon)

pygame.init()
WIDTH = HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


class initGraphics:
    def __init__(self) -> None:
        self.WIDTH = 700
        self.HEIGHT = 700

    def CreateChessBoard(self, WindowWidth, WindowHeight, surface):
        SpaceW = 70
        SpaceH = 70
        x = y = 10
        color = (255, 255, 255)
        white = (255, 255, 255)
        pink = (255, 153, 153)

        def create_horizontal_rects(x, y, color, color2):
            for i in range(8):
                rects = pygame.Rect(x, y, SpaceW, SpaceH)
                if i % 2 == 0:
                    pygame.draw.rect(surface, color, rects)
                    x += SpaceW
                else:
                    pygame.draw.rect(surface, color2, rects)
                    x += SpaceW
        x = 10
        for i in range(8):
            if i % 2 == 0:
                create_horizontal_rects(x, y, white, pink)
                y += SpaceH
            if i % 2 == 1:
                create_horizontal_rects(x, y, pink, white)
                y += SpaceW

    def button(self, window, position, text, font, size, color, color2):
        fg = color
        bg = color2
        font = pygame.font.SysFont(font, size)
        text_render = font.render(text, 1, fg)
        pos_x, pos_y, w, h = text_render.get_rect()
        pos_x, pos_y = position
        pygame.draw.line(window, (200, 200, 200),
                         (pos_x, pos_y), (pos_x + w, pos_y), 5)
        pygame.draw.line(window, (200, 200, 200),
                         (pos_x, pos_y - 2), (pos_x, pos_y + h), 5)
        pygame.draw.line(window, (50, 50, 50),
                         (pos_x, pos_y + h), (pos_x + w, pos_y + h), 5)
        pygame.draw.line(window, (50, 50, 50), (pos_x + w,
                         pos_y+h), [pos_x + w, pos_y], 5)
        pygame.draw.rect(window, bg, (pos_x, pos_y, w, h))
        return window.blit(text_render, (pos_x, pos_y))

    # function add button to the screen at position x,y with width and height w,h
    def addButton(self, window):
        buttonAstar = self.button(window, (200, 600), 'Solver Astar',
                                  'Corbel', 30, (255, 255, 255), (255, 153, 153))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.CreateChessBoard(self.WIDTH, self.HEIGHT, WINDOW)
            self.addButton(WINDOW)
            pygame.display.update()
