from ray import Ray
from player import Player
from math import *
import pygame

def distance(x1, y1, x2, y2):
  return ((x2-x1)**2 + (y2-y1)**2)**0.5 

wall_size = 50
p = Player()

lines = open('map.txt',"r").read().split("\n")
grid = [[int(c) for c in line] for line in lines]
print(grid)

#p.x = W/2
#p.y = H/2

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Python Raycaster")
 
done = False
 
clock = pygame.time.Clock()

do_map = True
wK = False
aK = False
sK = False
dK = False

while not done:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
          if do_map:
            do_map = False
          elif do_map == False:
            do_map = True
        if event.key == pygame.K_w:
          wK = True
        if event.key == pygame.K_s:
          sK = True
        if event.key == pygame.K_a:
          aK = True
        if event.key == pygame.K_d:
          dK = True
      
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
          wK = False
        if event.key == pygame.K_s:
          sK = False
        if event.key == pygame.K_a:
          aK = False
        if event.key == pygame.K_d:
          dK = False
  screen.fill((0,0,0))

  if wK:
    p.y -= 1
  if aK:
    p.x -= 1
  if sK:
    p.y += 1
  if dK:
    p.x += 1

  if do_map:
    for x, col in enumerate(grid):
      for y, tile in enumerate(col):
        if tile == 1:
          pygame.draw.rect(screen,(255,255,255),(x*50,y*50,wall_size,wall_size))
    pygame.draw.rect(screen,(255,0,0),(p.x,p.y,wall_size/2,wall_size/2))

  if do_map == False:
    ray = Ray()

    for c in range(p.fov):
      ray.angle = p.angle + c/p.fov
      ray.x = p.x 
      ray.y = p.y
      while True:
        ray.x += cos(ray.angle) * wall_size
        ray.y += sin(ray.angle) * wall_size
        gx = int(ray.x/wall_size)
        gy = int(ray.y/wall_size)
        if gx < 0 or gx > 9:
          break
        if gy < 0 or gy > 9:
          break
        tile = grid[gx][gy]
        if tile == 1:
          d = distance(p.x,p.y,ray.x,ray.y)
          h = d
          sx = (c/p.fov) * 500
          sy = 500 - h
          pygame.draw.rect(screen,(255,0,0),(sx,sy,500/p.fov,h))

          
          break

  pygame.display.update()
  pygame.display.flip()
  clock.tick(60)
 
pygame.quit()