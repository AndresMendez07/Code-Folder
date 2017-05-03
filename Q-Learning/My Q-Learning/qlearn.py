import pygame, sys
from pygame.locals import *

pygame.init()

tile_size = 80
grid_line_thickness = 2
screen_width = (tile_size*9) + grid_line_thickness
screen_height = (tile_size*8) + grid_line_thickness
DISPLAY=pygame.display.set_mode((screen_width,screen_height),0,32)

WHITE=(255,255,255)
blue=(0,0,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
orange=(255,140,0)




map = [[0,0,0,1,0,0,0,0,0,0],
       [0,0,0,1,0,0,1,1,0,0],
       [0,0,0,1,0,0,1,3,0,0],
       [0,0,0,0,0,0,1,0,0,0],
       [0,0,0,0,0,0,1,0,0,0],
       [0,0,0,1,0,0,1,2,0,0],
       [0,0,0,1,0,0,1,1,0,0],
       [0,0,0,1,0,0,0,0,0,0]]

DISPLAY.fill(WHITE)

def world():
  global tile_size
  
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] == 1:
        pygame.draw.rect(DISPLAY,black,(j*tile_size, i*tile_size,tile_size,tile_size))
      elif map[i][j] == 2:
        pygame.draw.rect(DISPLAY,green,(j*tile_size, i*tile_size,tile_size,tile_size))
      elif map[i][j] == 3:
        pygame.draw.rect(DISPLAY,red,(j*tile_size, i*tile_size,tile_size,tile_size))
      else:
        pygame.draw.rect(DISPLAY,WHITE,(j*tile_size, i*tile_size,tile_size,tile_size))
      
      pygame.draw.rect(DISPLAY,black,(j, i*tile_size,screen_width,grid_line_thickness))#horizontal grid lines
      pygame.draw.rect(DISPLAY,black,(j*tile_size, i,grid_line_thickness,screen_height))#vertical grid lines
      
def player_control():
  actions = ["up", "down", "left", "right"]
  if "up" in actions:
    try_move(0,-1)
  elif "down" in actions:
    try_move(0, 1)
  elif "left" in actions:
    try_move(-1,0)
  elif "right" in actions:
    try_move(1,0)
    
def try_move(x, y):
    x+=1;


while True:
  for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        sys.exit()
        
  pygame.display.update()
  world()


