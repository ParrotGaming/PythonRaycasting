from ray import Ray
from player import Player
from math import *
import pygame

wall_size = 50
p = Player()

lines = open('map.txt',"r").read().split("\n")
grid = [[int(c) for c in line] for line in lines]

#W = wall_size * len(grid)
#H = wall_size * len(grid[0])

#p.x = W/2
#p.y = H/2

print(grid)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Python Raycaster")
 
done = False
 
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill((0,0,0))

    p.angle += 0.1

    for c in range(60):
        a = p.angle - p.fov/2 + c * p.fov/500
        x = p.x
        y = p.y
        #Wrap This In a Loop
        while(0 <= x <= 500 and 0 <= y <= 500):
            gx = x // wall_size
            gy = y // wall_size
            tile = grid[int(gx)][int(gy)]
            if tile == 1:
                pygame.draw.line(screen, (255,255,255), (x,y), (x,500), 1)
                break
            x += cos(a)
            y += sin(a)

    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()