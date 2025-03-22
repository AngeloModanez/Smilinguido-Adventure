import pygame
from pygame.locals import *
import math

xSmilinguido, ySmilinguido = 425, 275
hSmilinguido, wSmilinguido = 50, 50

smilinguido = pygame.Rect(xSmilinguido, ySmilinguido, hSmilinguido, wSmilinguido)


def movementKeys(xSmilinguido, ySmilinguido):
    keys = pygame.key.get_pressed()
    mov_x = mov_y = 0
    speed = 10

    if keys[K_LEFT]:
        mov_x -= 1
    if keys[K_RIGHT]:
        mov_x += 1
    if keys[K_UP]:
        mov_y -= 1
    if keys[K_DOWN]:
        mov_y += 1

    if mov_x != 0 and mov_y != 0:
        mov_x /= math.sqrt(2)
        mov_y /= math.sqrt(2)

    xSmilinguido += mov_x * speed
    ySmilinguido += mov_y * speed

    return xSmilinguido, ySmilinguido
