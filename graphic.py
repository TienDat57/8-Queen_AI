from tkinter import W
import pygame
import sys
from pygame.locals import *

pygame.display.set_caption('8 Queens Problem')
Icon = pygame.image.load('queen.png')
pygame.display.set_icon(Icon)

pygame.init()


def CREATE_CHESSBOARD(window_width, window_height, surface):
    rect_width = 70
    rect_height = 70
    x = y = 10
    color = None
    white = (255, 255, 255)
    pink = (255, 153, 153)

    def create_horizontal_rects(x, y, color, color2):
        for i in range(8):
            rects = pygame.Rect(x, y, rect_width, rect_height)
            if i % 2 == 0:
                pygame.draw.rect(surface, color, rects)
                x += rect_width
            else:
                pygame.draw.rect(surface, color2, rects)
                x += rect_width
    x = 10
    for i in range(8):
        if i % 2 == 0:
            create_horizontal_rects(x, y, white, pink)
            y += rect_height
        if i % 2 == 1:
            create_horizontal_rects(x, y, pink, white)
            y += rect_width



WIDTH = HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        CREATE_CHESSBOARD(WIDTH, HEIGHT, WINDOW)
        smallfont = pygame.font.SysFont('Corbel',16) 
        text = smallfont.render('LOAD' , True , 'green')
        WINDOW.blit(text , (600 , 320))
        pygame.display.update()


mainloop()

