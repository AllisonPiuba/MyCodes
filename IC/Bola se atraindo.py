import pygame as pg
from random import randrange
import math
laranja=(255,140,0)	
preto=(0,0,0)
try:
        pg.init()
except:
    print("Deu ruim ai irmao")
    
largura = 640
altura = 400
pos_x=randrange(5, 640, 1)
pos_y=randrange(5, 400, 1)
pos_w=randrange(5, 640, 1)
pos_z=randrange(5, 400, 1)
c1 = [pos_x, pos_y]
c2 = [pos_w, pos_z]
sqrt = math.sqrt
deltax = (pos_x - pos_w)
deltay = (pos_y - pos_z)

def grav(deltax, deltay):
   i = sqrt((deltax)**2 + (deltay)**2)
   u = [(deltax/i) , (deltay/i)]

       
   
fundo = pg.display.set_mode((largura, altura))
pg.display.set_caption("bolinha se mexendo, ou quase")
mexer = True
opa = False
while mexer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mexer = False   
    fundo.fill(preto)        
    corpo1 = pg.draw.ellipse(fundo, laranja, [pos_x, pos_y, 40, 40])
    corpo2 = pg.draw.ellipse(fundo, laranja, [pos_w, pos_z, 40, 40])
    pg.display.update()
    corpo1 += pos_x + grav(u)
    
        
    
   

    
pg.quit()

