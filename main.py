from ray import Ray
from player import Player
from math import *
import pygame

def distance(x1, y1, x2, y2):
  return ((x2-x1)**2 + (y2-y1)**2)**0.5 

wall_colors = [
(0,0,0),
(255,0,0),
(0,255,0),
(0,0,255),
]

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

  speed = 0

  if wK:
    speed += 1
  if aK:
    p.angle -= .1
  if sK:
    speed -= 1
  if dK:
    p.angle += .1
  
  p.x += cos(p.angle + p.fov/2) * speed
  p.y += sin(p.angle + p.fov/2) * speed

  if do_map:
    for x, col in enumerate(grid):
      for y, tile in enumerate(col):
        if tile > 0:
          color = wall_colors[tile]
          pygame.draw.rect(screen,(color),(x*50,y*50,wall_size,wall_size))
    pygame.draw.rect(screen,(255,0,0),(p.x - wall_size/4 ,p.y - wall_size/4,wall_size/2,wall_size/2))
    # line(surface, color, start_pos, end_pos, width)
    a = (p.x + cos(p.angle) * wall_size/2, p.y + sin(p.angle) * wall_size/2)
    b = (p.x + cos(p.angle + p.fov) * wall_size/2, p.y + sin(p.angle + p.fov) * wall_size/2)
    pygame.draw.line(screen, (255,255,0),(p.x,p.y), a)
    pygame.draw.line(screen, (255,255,0),(p.x,p.y), b)
    # x = p.x + cos(p.angle) * wall_size / 2 - wall_size/8
    # y = p.y + sin(p.angle) * wall_size / 2 - wall_size/8
    # pygame.draw.rect(screen,(255,255,0),(x,y,wall_size/4,wall_size/4))

  if do_map == False:
    ray = Ray()

    for c in range(500):
      ray.angle = p.angle + p.fov * c/500
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
        if tile > 0:
          color = wall_colors [tile]
          d = distance(p.x,p.y,ray.x,ray.y)
          h = 500 - d
          sx = c
          sy = 500 - h
          pygame.draw.rect(screen,color,(sx,sy,500/p.fov,h))

          
          break

  pygame.display.update()
  pygame.display.flip()
  clock.tick(60)
 
pygame.quit()