import pygame
import numpy as np


pygame.init()

gridSize = (60, 60)
pixel = 8

scrnSiz = (gridSize[0]  * pixel, gridSize[1] * pixel)
scrn = pygame.display.set_mode(scrnSiz)
black = (0, 0, 0)
white = (255, 255, 255)

grid = np.zeros(gridSize, dtype=int)




running = True
while running:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
        elif even.type == pygame.MOUSEBUTTONDOWN or even.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                mousePos = pygame.mouse.get_pos()
                x, y = mousePos[0] // pixel, mousePos[1] // pixel
                grid[y, x] = 1
    scrn.fill(white)

    for y in range(gridSize[0]):
        for x in range(gridSize[1]):
            color = black if grid[y, x] == 1 else white
            pygame.draw.rect(scrn, color, (x * pixel, y * pixel, pixel, pixel))
        
    pygame.display.flip()
pygame.quit()