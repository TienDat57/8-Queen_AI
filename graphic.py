import tkinter
import pygame
import sys
from curses import COLOR_WHITE, window
from pygame.locals import *
from program import Program
from tkinter import filedialog

SIZE_SPACE = 70
WIDTH = 560
HEIGHT = 650
IMAGE = {}
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (204, 255, 102)


def load_image():
    IMAGE['queen'] = pygame.transform.scale(
        pygame.image.load("queen.png"), (SIZE_SPACE, SIZE_SPACE))


def draw_queen(window, queens):
    for(x, y) in queens:
        window.blit(IMAGE['queen'], pygame.Rect(
            x * SIZE_SPACE, y * SIZE_SPACE, SIZE_SPACE, SIZE_SPACE))

def open_dialog_path():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    nameFile = filedialog.askopenfilenames(filetypes=[("Text Files", ".txt")])
    return nameFile


def create_chess_board(window, queens):
    x = y = 0

    def create_horizontal_rects(x, y, color, color2):
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
            create_horizontal_rects(x, y, COLOR_WHITE, COLOR_YELLOW)
            y += SIZE_SPACE
        if i % 2 == 1:
            create_horizontal_rects(x, y, COLOR_YELLOW, COLOR_WHITE)
            y += SIZE_SPACE
    if len(queens) > 1:
        draw_queen(window, queens)


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


def run(pr: Program):
    load_image()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()
    pygame.display.set_caption('8 Queens Problem')
    Icon = pygame.image.load('queen.png')
    pygame.display.set_icon(Icon)
    buttonSolve = button(WINDOW, (200, 580), 'Solve CNF',
                         'Corbel', 30, 'red', COLOR_WHITE)
    buttonInputFile = button(
        WINDOW, (400, 580), 'Input File', 'Corbel', 30, COLOR_WHITE, 'gray')
    running = True
    resPos = [()]
    nameFile = ''
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if buttonSolve.collidepoint(pos):
                        print("oik")                            
                    if buttonInputFile.collidepoint(pos):
                        nameFile = open_dialog_path()
                        resPos = pr.readFile(nameFile[0])
                    else:
                        print('No button clicked')
        create_chess_board(WINDOW, resPos)
        pygame.display.update()
