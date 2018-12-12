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
G = 6.673*10**(11)

def delta (x1, x2):
    return x1 - x2

def grav(corpos):
   d = np.zeros( (n,n) ) 
   ux =  np.zeros( (n,n) ) 
   uy =  np.zeros( (n,n) )
   F =  np.zeros( (n,n) )
   Acc1 = np.zeros( (n,n) )
   Acc2 = np.zeros( (n,n) )
   for i in range (n):
       for j in range (n):
           deltax = (corpos[i][0] - corpos[j][0])  
           deltay = (corpos[i][1] - corpos[j][1])
           d[i][j] = math.sqrt((deltax)**2 + (deltay)**2)
           if not i == j:
               ux[i][j] = deltax/d[i][j]
               uy[i][j] = deltay/d[i][j]
               F[i][j] = (G * corpos[i][2] * corpos[j][2])/d[i][j]**2
               Acc1[i][j] = F[i][j]/corpos[i][2]
               Acc2[i][j] = F[i][j]/corpos[j][2]
           else:
               ux[i][j] = uy[i][j] = 0
               F[i][j] = 0
               Acc1[i][j] = Acc2[i][j] = 0
               
           
  
   
   # may the force be with you
      
   return d, ux, uy, F, Acc1, Acc2




#%%
fundo = pg.display.set_mode((largura, altura))
pg.display.set_caption("N-Corpos, ou quase")
#%%

coordenadas_x = np.random.randint(0, largura, (n,1))
coordenadas_y = np.random.randint(0, altura, (n,1))
massa = np.random.randint(tamanho_min, tamanho_max, (n,1))
corpos = np.hstack([coordenadas_x, coordenadas_y, massa])

D, ux, uy, F, Acc1, Acc2 = grav(corpos)

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