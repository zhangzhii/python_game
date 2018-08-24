import math
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2

piece1 = False
piece2 = False
piece3 = False
piece4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True

    screen.fill((202,225,255))

    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x+radius/2-20, y-radius/2))
    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x - radius / 2, y - radius / 2))
    textImg1 = myfont.render("3", True, color)
    screen.blit(textImg1, (x - radius / 2, y + radius / 2-20))
    textImg1 = myfont.render("4", True, color)
    screen.blit(textImg1, (x + radius / 2 - 20, y + radius / 2-20))

    if piece1:
        angle_start = math.radians(0)
        angle_end = math.radians(90)
        pygame.draw.arc(screen, color, position, angle_start, angle_end, width)
        pygame.draw.line(screen,color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen,color, (x,y), (x+radius, y), width)

    if piece2:
        angle_start = math.radians(90)
        angle_end = math.radians(180)
        pygame.draw.arc(screen, color, position, angle_start, angle_end, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)

    if piece3:
        angle_start = math.radians(180)
        angle_end = math.radians(270)
        pygame.draw.arc(screen, color, position, angle_start, angle_end, width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)

    if piece4:
        angle_start = math.radians(270)
        angle_end = math.radians(360)
        pygame.draw.arc(screen, color, position, angle_start, angle_end, width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)

    if piece1 and piece2 and piece3 and piece4:
        color = 0, 255, 0

    pygame.display.update()
