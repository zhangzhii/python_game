import sys, pygame, math, random
from pygame.locals import *

white = 255,255,255
blue = 202,225,255
pink = 255, 0,0

position = 300, 250
radius = 50
width = 10

pos = 400,500,50,50
pos_x = 400
pos_y = 500
vel_x = 2
vel_y = 2



pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Draw something @^@")
color = white
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys, exit()
    screen.fill(blue)
    # pygame.draw.circle(screen,white,position, radius,width)

    pos_x += vel_x
    pos_y += vel_y

    if pos_x >= 1000 or pos_x < 0:
        vel_x = -vel_x
        color = pink
    if pos_y >= 800 or pos_y < 0:
        vel_y = -vel_y
        color = pink

    pos = pos_x, pos_y
    # pygame.draw.rect(screen,white,pos,0)
    pygame.draw.circle(screen,color,pos, radius,0)
    # pygame.draw.line(screen,white,(100,100),(200,200),width)

    start_angle = math.radians(0)
    end_angle = math.radians(180)
    # pygame.draw.arc(screen, white, (200,100,200,300), start_angle, end_angle, 5)

    # pygame.draw.ellipse(screen, white, (100, 100, 200, 100), 0)
    pygame.draw.line(screen, white, (random.randint(0,1000),random.randint(0,800)), (random.randint(0,1000),random.randint(0,800)),5)


    pygame.display.update()
