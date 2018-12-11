import pygame as pg
import math
import numpy as np

laranja=(255,140,0)	
preto=(0,0,0)
red=(255,0,0)
try:
    pg.init()
except:
    print("Deu ruim ai irmao")
    

n = 10
largura = 1024
altura = 720
tamanho_min = 5
tamanho_max = 15
G = G = 6.673*10**(2)

def delta (x1, x2):
    return math.abs(x1 - x2)

def grav(deltax, deltay, m1, m2):
   d = np.zeros( (n,n) ) 
   for i in range (n):
       for j in range (n):
           math.sqrt((deltax)**2 + (deltay)**2)
           u = [(deltax/d) , (deltay/d)]
   
   
   # may the force be with you
   F = (G * m1 * m2)/d**2
   
   return d, u, F




#%%
fundo = pg.display.set_mode((largura, altura))
pg.display.set_caption("N-Corpos, ou quase")
#%%

coordenadas_x = np.random.randint(0, largura, (n,1))
coordenadas_y = np.random.randint(0, altura, (n,1))
massa = np.random.randint(tamanho_min, tamanho_max, (n,1))
corpos = np.hstack([coordenadas_x, coordenadas_y, massa])

#%%
troca_em_x = False
troca_em_y = False
colisao = False
mexer = True

while mexer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mexer = False   
    fundo.fill(preto)     

    if (colisao or troca_em_x or troca_em_y):
        print("noo")   
    else:
        
        
        for x, y, tamanho in corpos:
            pg.draw.circle(fundo, laranja, [x, y], tamanho)        
    
    pg.display.update()        
    pg.time.wait(45)

pg.quit()