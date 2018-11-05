import pygame as pg
from random import randrange
import math

laranja=(255,140,0)	
preto=(0,0,0)
try:
        pg.init()
except:
    print("Deu ruim ai irmao")
    

def grav(deltax, deltay):
   i = math.sqrt((deltax)**2 + (deltay)**2)
   u = [(deltax/i) , (deltay/i)]
   
   return u
    
largura = 640
altura = 400
tamanho=5
linha=  1
pos_x=randrange(5, 640, 1)
pos_y=randrange(5, 400, 1)
pos_w=randrange(5, 640, 1)
pos_z=randrange(5, 400, 1)

fundo = pg.display.set_mode((largura, altura))
pg.display.set_caption("bolinha se mexendo, ou quase")


mexer = True
opa = False
while mexer:
    #for event in pg.event.get():
    #    if event.type == pg.QUIT:
    #        mexer = False   
    fundo.fill(preto)       
    #pg.draw.rect(fundo,laranja,[pos_x, pos_y,tamanho,tamanho])
    bolota1 = pg.draw.circle(fundo, laranja, [pos_x, pos_y], tamanho)
    bolota2 = pg.draw.circle(fundo, laranja, [pos_w, pos_z], tamanho)
    
    deltax = (pos_x - pos_w)
    deltay = (pos_y - pos_z)
    
    pg.display.update()
    
    u = grav(deltax, deltay)
    
    pos_x -= int(u[0] * 100)
    pos_y -= int(u[1] * 100)
    
    pos_w += int(u[0] * 100)
    pos_z += int(u[1] * 100)


    if pos_x == largura:
        pos_x += -640
    if pos_y == altura:
        pos_y += -400
        
    pg.time.wait(1000)
        
        ##Os coments abaixo sao um problema a ser resolvido para conseguir 
        #fazer a bola ir e voltar em loop 
        
        #mexer = False
        #opa = True
#while opa:
    #for event in pg.event.get():
        #if event.type == pg.QUIT:
            #opa = False   
    #fundo.fill(preto)       
    #pg.draw.rect(fundo,laranja,[pos_x, pos_y,tamanho,tamanho])
   # pg.draw.circle(fundo, laranja, [pos_x, pos_y], tamanho)
    #pg.display.update()
    #pos_x+=-1

pg.quit()
