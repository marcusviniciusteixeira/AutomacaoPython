import pygame
from pygame.locals import *

pygame.init()

largura = 800
altura = 600

x = int(largura/2)
y = int(altura/2)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('teste')

GRAY = (50,50,70)
RED = (100,0,0)
BLUE = (0,0,100)

while True:
    tela.fill(GRAY)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
           
    player = pygame.draw.circle(tela, BLUE, (x, y), 12)
            
            
    pygame.display.flip()