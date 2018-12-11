import pygame as pg
from random import randrange
import math

laranja=(255,140,0)	
preto=(0,0,0)
red=(255,0,0)
try:
        pg.init()
except:
    print("Deu ruim ai irmao")
    

def grav(deltax, deltay, m1, m2):
   d = math.sqrt((deltax)**2 + (deltay)**2)
   u = [(deltax/d) , (deltay/d)]
   G = 6.673*10**(2)
   
   # may the force be with you
   F = (G * m1 * m2)/d**2
   
   return d, u, F

largura = 1024
altura = 720
tamanho1=randrange(5, 15) 
tamanho2=randrange(5, 15)
m1 = tamanho1
m2 = tamanho2
vel1 = 0
vel2 = 0
acc1 = 0
acc2 = 0

pos_x=randrange(5, largura)
pos_y=randrange(5, altura)
pos_w=randrange(5, largura)
pos_z=randrange(5, altura)

tamanho3 = tamanho1 + tamanho2

fundo = pg.display.set_mode((largura, altura))
pg.display.set_caption("bolinha se mexendo, ou quase")


mexer = True
opa = False

pos_x_anterior = pos_x
pos_y_anterior = pos_y
pos_w_anterior = pos_w
pos_z_anterior = pos_z
troca_em_x = False
troca_em_y = False
colisao = False

while mexer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mexer = False   
    fundo.fill(preto)     
    
    deltax = (pos_x - pos_w)
    deltay = (pos_y - pos_z)
    
    if (pos_x >= pos_w and pos_x_anterior < pos_w_anterior):
        troca_em_x = True
        
    if (pos_y >= pos_z and pos_y_anterior < pos_z_anterior):
        troca_em_y = True
 
    d, u, F = grav(deltax, deltay, m1, m2)
    
    colisao = d <= tamanho1 + tamanho2
    
    pos_x_anterior = pos_x
    pos_y_anterior = pos_y
    pos_w_anterior = pos_w
    pos_z_anterior = pos_z
    
    
    if (colisao or troca_em_x or troca_em_y):
             
        if tamanho1 > tamanho2:
            bolota3 = pg.draw.circle(fundo, red, [pos_x, pos_y], tamanho3)
        else:
            bolota3 = pg.draw.circle(fundo, red, [pos_w, pos_z], tamanho3)
        
    else:
        
        acc1 = F / m1
        acc2 = F / m2
        
        vel1 = vel1 + acc1
        vel2 = vel2 + acc2
        
        pos_x -= int(u[0] * (vel1)*10)
        pos_y -= int(u[1] * (vel1)*10)
        
        pos_w += int(u[0] * (vel2)*10)
        pos_z += int(u[1] * (vel2)*10)
    
    
        if pos_x == largura:
            pos_x += -640
        if pos_y == altura:
            pos_y += -400
        
        bolota1 = pg.draw.circle(fundo, laranja, [pos_x, pos_y], tamanho1)
        bolota2 = pg.draw.circle(fundo, laranja, [pos_w, pos_z], tamanho2)  
        
    
    pg.display.update()        
    pg.time.wait(45)

pg.quit()
