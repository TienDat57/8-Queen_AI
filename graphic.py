from curses import COLOR_WHITE, window
import pygame
import sys
from pygame.locals import *
from program import Program

SIZE_SPACE = 70
WIDTH = HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGE = {}
COLOR_WHITE = (255, 255, 255)
COLOR_PINK = (255, 153, 153)


def loadImage():
    IMAGE['queen'] = pygame.transform.scale(
        pygame.image.load("queen.png"), (SIZE_SPACE, SIZE_SPACE))


def drawQueen(window, queens):
    print(queens)
    # for(x, y) in queens:
    #     window.blit(IMAGE['queen'], pygame.Rect(x * SIZE_SPACE, y * SIZE_SPACE, SIZE_SPACE, SIZE_SPACE))
    # screen.blit(IMAGE['queen'], pygame.Rect(
    #     queens[0][1]*SIZE_SPACE, queens[0][0]*SIZE_SPACE, SIZE_SPACE, SIZE_SPACE))


def CreateChessBoard(window, queens):
    x = y = 0

    def createHorizontalRects(x, y, color, color2):
        for i in range(8):
            rects = pygame.Rect(x, y, SIZE_SPACE, SIZE_SPACE)
            if i % 2 == 0:
                pygame.draw.rect(window, color, rects)
                x += SIZE_SPACE
            else:
                pygame.draw.rect(window, color2, rects)
                x += SIZE_SPACE
    x = 0
    for i in range(8):
        if i % 2 == 0:
            createHorizontalRects(x, y, COLOR_WHITE, COLOR_PINK)
            y += SIZE_SPACE
        if i % 2 == 1:
            createHorizontalRects(x, y, COLOR_PINK, COLOR_WHITE)
            y += SIZE_SPACE
    for(x, y) in queens:
        print(x[0], y[0])
    # window.blit(IMAGE['queen'], pygame.Rect(x * SIZE_SPACE, y * SIZE_SPACE, SIZE_SPACE, SIZE_SPACE))


def button(window, position, text, font, size, color, color2):
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


def addButton(window):
    return button(window, (200, 600), 'Solve CNF', 'Corbel', 30, COLOR_PINK, COLOR_WHITE)


def run():
    loadImage()
    pr = Program(8)
    pygame.init()
    pygame.display.set_caption('8 Queens Problem')
    Icon = pygame.image.load('queen.png')
    pygame.display.set_icon(Icon)
    buttonSolve = addButton(WINDOW)
    running = True
    resPos = [()]
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if buttonSolve.collidepoint(pos):
                        resPos = pr.readFile("./Input/input1.txt")
                        print(resPos)
                        # solveAstar()
                    else:
                        print('No button clicked')
        CreateChessBoard(WINDOW, resPos)
        pygame.display.update()
