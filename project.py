import pygame
import ambient as ambient
import sprites.character as character
from ambient import running, screen, fps
from sprites.character import (
    xSmilinguido,
    ySmilinguido,
    hSmilinguido,
    wSmilinguido,
)

pygame.init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.rect(screen, ("gray"), character.smilinguido)

    character.smilinguido.x = xSmilinguido
    character.smilinguido.y = ySmilinguido

    xSmilinguido, ySmilinguido = character.movementKeys(xSmilinguido, ySmilinguido)
    xSmilinguido, ySmilinguido, hSmilinguido, wSmilinguido = ambient.movementBoundary(
        xSmilinguido, ySmilinguido, hSmilinguido, wSmilinguido
    )

    pygame.display.update()
    fps.tick(30)

pygame.quit()
