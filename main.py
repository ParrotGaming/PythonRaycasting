from ray import Ray
from player import Player
from math import *
import pygame

wall_size = 50
p = Player()

lines = open('map.txt',"r").read()
grid = [[int(c) for c in line] for line in lines]

#p.x = W/2
#p.y = H/2

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Python Raycaster")
 
done = False
 
clock = pygame.time.Clock()

screen.fill((0,0,0))

pos = 0
y = 0
for c in lines:
  x = (pos)
  pos += 1
  if pos == 10:
    pos = 0
    y += 1
    
  if c == "1":
    pygame.draw.rect(screen,(255,255,255),(x*50,y*50,wall_size,wall_size))
    pygame.display.update()
    print(x,y)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # for c in range(500):
    #     a = p.angle - p.fov/2 + c * p.fov/500
    #     x = p.x
    #     y = p.y
    #     #Wrap This In a Loop
    #     while(0 <= x <= 500 and 0 <= y <= 500):
    #         gx = x // wall_size
    #         gy = y // wall_size
    #         tile = grid[int(gx)][int(gy)]
    #         if tile == 1:
    #             pygame.draw.line(screen, (255,255,255), (c,0), (c,500), 1)
    #             break
    #         x += cos(a)
    #         y += sin(a)

    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()