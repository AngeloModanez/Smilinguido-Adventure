import pygame
import sys
from pygame.locals import *

fps = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((900, 600))


def movementBoundary(mov_x, mov_y, cha_h, cha_w):
    if mov_x < 0:
        mov_x = 0
    if mov_x > 900 - cha_h:
        mov_x = 900 - cha_h
    if mov_y < 0:
        mov_y = 0
    if mov_y > 600 - cha_w:
        mov_y = 600 - cha_w
    return mov_x, mov_y, cha_h, cha_w
