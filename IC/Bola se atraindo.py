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
    

def grav(deltax, deltay):
   d = math.sqrt((deltax)**2 + (deltay)**2)
   u = [(deltax/d) , (deltay/d)]
   
   return d, u

largura = 1024
altura = 720
tamanho1=randrange(5, 15)
tamanho2=randrange(5, 15)

linha=  1
pos_x=randrange(5, largura)
pos_y=randrange(5, altura)
pos_w=randrange(5, largura)
pos_z=randrange(5, altura)

tamanho3 = tamanho1 + tamanho2

fundo = pg.display.set_mode((largura, altura))
pg.display.set_caption("bolinha se mexendo, ou quase")


mexer = True
opa = False
while mexer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mexer = False   
    fundo.fill(preto)       
    #pg.draw.rect(fundo,laranja,[pos_x, pos_y,tamanho,tamanho])
    ##fazer elipse como alternativa de solução de numeros reais
    deltax = (pos_x - pos_w)
    deltay = (pos_y - pos_z)
    
    d, u = grav(deltax, deltay)
    
    if (d <= tamanho1 + tamanho2):
        #bolota1 = pg.draw.circle(fundo, preto, [pos_x, pos_y], tamanho1)
        #bolota2 = pg.draw.circle(fundo, preto, [pos_w, pos_z], tamanho2)

        if tamanho1 > tamanho2:
            bolota3 = pg.draw.circle(fundo, red, [pos_x, pos_y], tamanho3)
        else:
            bolota3 = pg.draw.circle(fundo, red, [pos_w, pos_z], tamanho3)
        
    else:
        
        vel1 = 5
        vel2 = 5
        
        pos_x -= int(u[0] * vel1)
        pos_y -= int(u[1] * vel1)
        
        pos_w += int(u[0] * vel2)
        pos_z += int(u[1] * vel2)
    
    
        if pos_x == largura:
            pos_x += -640
        if pos_y == altura:
            pos_y += -400
        
        bolota1 = pg.draw.circle(fundo, laranja, [pos_x, pos_y], tamanho1)
        bolota2 = pg.draw.circle(fundo, laranja, [pos_w, pos_z], tamanho2)  
        
    
    pg.display.update()        
    pg.time.wait(60)
    
        
            

pg.quit()
