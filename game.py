# Bibliotecas
import pygame

from sys import exit
#Janela
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('A janela')
clock = pygame.time.Clock()
fonte_teste = pygame.font.Font('font\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics\Sky.png')
ground_surface = pygame.image.load('graphics\ground.png')
text_surface = fonte_teste.render('My game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Camadas
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60)
